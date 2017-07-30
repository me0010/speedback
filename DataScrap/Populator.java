import java.io.BufferedReader;
import java.io.DataOutputStream;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;
import java.io.BufferedReader;
import java.io.File;
import java.io.FileReader;
import java.io.IOException;
class Populator{
  public static void main(String[] args){
    try {
			File file = new File("CleanVICData.csv");
			FileReader fileReader = new FileReader(file);
			BufferedReader bufferedReader = new BufferedReader(fileReader);
			StringBuffer stringBuffer = new StringBuffer();
			String line;
			while ((line = bufferedReader.readLine()) != null) {
        String[] parts = line.split(",");
        add(parts[3],parts[4],parts[0],parts[2],parts[1]);
				stringBuffer.append(line);
				stringBuffer.append("\n");
			}
			fileReader.close();
			System.out.println("Contents of file:");
			System.out.println(stringBuffer.toString());
		} catch (IOException e) {
    //add("12.2","12.5","234","120","Hambrook lane");
  }
  }
  private static void add(String lat, String lng, String signId, String limit, String roadName){
    try{
      String url = "http://speedback-17.appspot.com/newsign?lat=" +
        lat +"&lng=" + lng + "&signId=" + signId + "&speedlimit=" + limit + "&roadname=" + URLEncoder.encode(roadName);
      URL obj = new URL(url);
      HttpURLConnection con = (HttpURLConnection) obj.openConnection();
      con.setRequestMethod("GET");
      con.setRequestProperty("User-Agent", "Mozilla/5.0");
      int responseCode = con.getResponseCode();
    } catch (Exception e){
      //
    }
  }
}
