import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.Arrays;

public class BOJ_1377 {

    private static Number[] arr;
    static class Number implements Comparable<Number> {
        int number;
        int index;

        Number(int number, int index) {
            this.number = number;
            this.index = index;
        }

        @Override
        public int compareTo(Number o) {
            return this.number - o.number;
        }
    }
    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        arr = new Number[N];
        for (int idx = 0; idx < N; idx++) {
            arr[idx] = new Number(Integer.parseInt(br.readLine()), idx);
        }

        Arrays.sort(arr);

        int max = 0;
        for (int idx = 0; idx < N; idx++) {
            if (max < arr[idx].index - idx)
                max = arr[idx].index - idx;
        }
        System.out.println(max+1);
    }

}
