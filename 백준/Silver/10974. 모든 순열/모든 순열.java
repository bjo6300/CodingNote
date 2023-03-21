import java.io.*;

public class Main {
    public static int N;
    public static int[] arr;
    public static boolean[] visited;
    public static StringBuilder sb = new StringBuilder();

    public static void main(String[] args) throws IOException {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        N = Integer.parseInt(br.readLine());
        arr = new int[N]; 
        visited = new boolean[N]; // 방문 여부를 나타내는 배열

        permutation(0);
        System.out.println(sb);
    }

    public static void permutation(int depth) {
        if(depth == N) {
            for(int i=0; i<N; i++)
                sb.append(arr[i]).append(" ");

            sb.append("\n");
            return;
        }

        for(int i=0; i<N; i++) {
            if(visited[i])
                continue;

            arr[depth] = i + 1; // depth가 0부터 시작하므로 +1
            visited[i] = true;
            permutation(depth + 1);
            visited[i] = false;
        }
    }
}
