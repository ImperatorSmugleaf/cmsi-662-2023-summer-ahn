import java.util.Scanner;
import java.text.Normalizer;
import java.text.Normalizer.Form;
import java.util.regex.Pattern;
import java.util.regex.Matcher;

public class ids01 {
    public static void main(String[] args) {
        String myWebsiteStart = """
                <html>
                <body>
                """;
        String myWebsiteEnd = """
                </body>
                </html>
                """;
        Scanner scanner = new Scanner(System.in);

        System.out.println("Tell me your name.");
        String userName = scanner.nextLine();
        scanner.close();

        String normalizedName = Normalizer.normalize(userName, Form.NFKC);
        Pattern illegalTag = Pattern.compile("[<>]");
        Matcher htmlFinder = illegalTag.matcher(normalizedName);
        if (htmlFinder.find()) {
            throw new IllegalStateException("Names cannot contain html tags.");
        }

        System.out.println(myWebsiteStart + "<h1> welcome to my website, " + normalizedName + "! </h1>\n" + myWebsiteEnd);

    }
}
