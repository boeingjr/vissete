package no.boeingjr.vissete.spark;

import no.boeingjr.vissete.Version;
import static no.boeingjr.vissete.spark.JsonUtil.*;

import static spark.Spark.*;
import spark.Request;
import spark.Response;
import com.google.gson.Gson;
import com.google.gson.JsonObject;
import com.google.gson.JsonArray;


/**
 * Hello world!
 *
 */
public class SparkService
{
    public static Gson gson = new Gson();

    public SparkService()
    {
	before((req, res) -> {
		System.out.println("SparkService: " + req.requestMethod() + " " + req.pathInfo());
	    });
        get("/", (req, res) -> getRoot(req, res), json());
        get("/test", (req, res) -> getTest(req, res), json());
        post("/test", (req, res) -> postTest(req, res), json());
	after((req, res) -> {
		res.type("application/json");
	    });
    }

    private JsonObject getRoot(Request req, Response res) {
	JsonObject jo = new JsonObject();
	String rootInfo = "Vissete version " + Version.Version + " build " + Version.Build;
	jo.addProperty("data", rootInfo);
	return jo;
    }

    private JsonObject getTest(Request req, Response res) {
	JsonObject jo = new JsonObject();
	String rootInfo = "Vissete version " + Version.Version + " build " + Version.Build;
	jo.addProperty("data", rootInfo);
	jo.addProperty("request-body", gson.toJson(req.body()));
	jo.addProperty("request-query-params", gson.toJson(req.queryParams()));
	jo.addProperty("request-params", gson.toJson(req.params()));
	jo.addProperty("request-path", gson.toJson(req.pathInfo()));
	jo.addProperty("request-attributes", gson.toJson(req.attributes()));
	return jo;
    }

    private JsonObject postTest(Request req, Response res) {
	JsonObject jo = new JsonObject();
	String rootInfo = "Vissete version " + Version.Version + " build " + Version.Build;
	jo.addProperty("data", rootInfo);
	jo.addProperty("request-body", gson.toJson(req.body()));
	jo.addProperty("request-query-params", gson.toJson(req.queryParams()));
	jo.addProperty("request-params", gson.toJson(req.params()));
	jo.addProperty("request-path", gson.toJson(req.pathInfo()));
	jo.addProperty("request-attributes", gson.toJson(req.attributes()));
	return jo;
    }
}
