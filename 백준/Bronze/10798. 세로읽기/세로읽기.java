import java.io.*;
import java.util.*;

public class Main {
    private static void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuffer sb = new StringBuffer();
        char[][] arr = new char[5][15];

        for (int i = 0; i < arr.length; i++) {
            String input = br.readLine();
            for (int j = 0; j < input.length(); j++) {
                arr[i][j] = input.charAt(j); // 지정된 위치의 문자를 알려준다.
            }
        }

        for (int i = 0; i < 15; i++) {
            for (int j = 0; j < 5; j++) {
                if (arr[j][i] == '\0') // char의 초기 값 : \0 = null
                    continue;
                sb.append(arr[j][i]);
            }
        }
        System.out.println(sb);

    }
    public static void main(String[] args) throws Exception {
        solution();
    }
}