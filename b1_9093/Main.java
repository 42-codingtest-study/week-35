package b1_9093;
import java.io.BufferedReader;
import java.io.InputStreamReader;
import java.util.Arrays;
import java.util.StringTokenizer;

public class Main {
    private int n;
    private BufferedReader br;
    private StringTokenizer st;
    public static void main(String[] args) throws Exception {
        b1_9093.Main Main = new b1_9093.Main();
        Main.method();
    }
    public void method() throws Exception {
        br = new BufferedReader(new InputStreamReader(System.in));
        n = br.read();
        for(int i = 0; i < n; i++) {
            st = new StringTokenizer(br. readLine());
            char[][] arr = new char[st.countTokens()][];
            System.out.println(st.countTokens());
            for(int j = 0; j < st.countTokens(); j++) {
                arr[j] = st.nextToken().toCharArray();
                System.out.println(Arrays.toString(arr[j][]);
            }
        }
    }

}
