/**
 * Created by James on 2/05/2018.
 */
import java.util.*;
public class Load
{
	public static Map<String, Route> loadRoutes()
	{
		Map<String, Route> routeMap = new HashMap<String, Route>();
		String routeData = GeoUtils.retrieveRouteData();
		String[] dataArray = routeData.split("\n");
		//String[] entryArray;
		int arrayLength = dataArray.length;
		Route currRoute = new Route();
		String line;
		String routeName;
		for (int i = 0; i < arrayLength; i++) //first the empty routes will be constructed i.e no waypoints added yet
		{
			line = dataArray[i];
			if (line.matches("^[A-z].*$")) //if the line starts with a letter
			{
				Route newRoute = createNewRoute(line);
				routeMap.put(newRoute.getName(), newRoute);
			}
		}
		for(int i = 0; i < arrayLength; i++) //now the segments that make up the routes are added
		{
			line = dataArray[i];
			line.replace("\t", "");
			if (line.matches("^[A-z].*$"))
			{
				routeName = line.split(" ")[0];
				currRoute = routeMap.get(routeName);
			}else if((line.split(",").length > 2) && (!line.equals("\n")))
			{
				Segment newSegment = createNewSegment(line, routeMap);
				currRoute.addSegment(newSegment);
			}
		}
		return routeMap;
	}

	private static Route createNewRoute(String line)
	{
		String[] entryArray = line.split(" "); //What if description has spaces in it, MUST FIX
		String name = entryArray[0];
		String description = entryArray[1];
		description.replace("[", "").replace("]","");
		Route newRoute = new Route();
		newRoute.setName(name);
		newRoute.setDescription(description);
		return newRoute;
	}

	private static Segment createNewSegment(String line, Map<String, Route> routeMap)
	{
		Segment newSegment = new Waypoint();
		Waypoint newWaypoint;
		double inLat, inLong, inAlt;
		String inDesc;
		String[] entryArray = line.split(",");
		System.out.println("length is: " + entryArray.length);
		System.out.println(entryArray[0]);
		if(entryArray.length == 3) //is the line a waypoint at the end of a route?
		{
			inLong = Double.valueOf(entryArray[0]);
			inLat = Double.valueOf(entryArray[1]);
			inAlt = Double.valueOf(entryArray[2]);
			newWaypoint = new Waypoint(inLat, inLong, inAlt, "END OF ROUTE");
			newSegment = newWaypoint;
		}else if(entryArray[3].matches("[*].*$")) //is this a subroute?
		{
			String key = entryArray[3].replace("*", "");
			newSegment = routeMap.get(key);
		}else// if(entryArray[3].matches("[^\\[].*$]"))
		{
			inLong = Double.valueOf(entryArray[0]);
			inLat = Double.valueOf(entryArray[1]);
			inAlt = Double.valueOf(entryArray[2]);
			inDesc = entryArray[3];
			newWaypoint = new Waypoint(inLat, inLong, inAlt, inDesc);
			newSegment = newWaypoint;
		}
		return newSegment;
	}
}
