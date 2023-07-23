import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class BOJ_2750 {

    private static int[] arr;
    public static void main(String[] args) throws IOException {

        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        int N = Integer.parseInt(br.readLine());

        generateArr(br, N);

        BOJ_2750 bubbleSortPrinter = new BOJ_2750();
        bubbleSortPrinter.sortBubble(N);
        bubbleSortPrinter.printResult(N);
    }

    private void printResult(int N) {
        for (int idx = 0; idx < N; idx++) {
            System.out.println(arr[idx]);
        }
    }

    private void sortBubble(int N) {
        boolean isSwap = false;
        for (int idx = 0; idx < N - 1; idx++) {
            isSwap = false;
            int tmp = 0;
            for (int jdx = 0; jdx < N - 1 - idx; jdx++) {
                if (arr[jdx] > arr[jdx + 1]) {
                    tmp = arr[jdx];
                    arr[jdx] = arr[jdx + 1];
                    arr[jdx + 1] = tmp;
                    isSwap = true;
                }
            }
            if (!isSwap)
                break;
        }
    }

    private static void generateArr(BufferedReader br, int N) throws IOException {
        arr = new int[N];
        for (int idx = 0; idx < N; idx++) {
            arr[idx] = Integer.parseInt(br.readLine());
        }
    }
}
