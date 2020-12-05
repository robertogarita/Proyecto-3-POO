package jsonPrueba;

import org.json.*;

public class Sandbox {

    public static void main(String[] args) {

        JSONObject myObject = new JSONObject();
        JSONArray myArray = new JSONArray();

        myObject.put("name", "Carlos");
        myObject.put("last_name", "Jose");
        myObject.put("fuck_you", "tony");

        myArray.put(5);
        myArray.put(5.6);
        myArray.put("Hola");
    }

}
