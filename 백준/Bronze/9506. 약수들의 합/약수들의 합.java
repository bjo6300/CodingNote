import java.io.*;
import java.util.*;

public class Main {
    private static void solution() throws Exception {
        BufferedReader br = new BufferedReader(new InputStreamReader(System.in));
        StringBuffer sb = new StringBuffer();
        List<Integer> inputList = new ArrayList<Integer>();

        while(true) {
            int input = Integer.parseInt(br.readLine()); // int형으로 받기
            int sum = 0;
            inputList.clear(); // 리스트 내부 초기화
            sb.setLength(0); // StringBuffer 초기화

            if(input == -1) { // -1이 들어온 경우
                break;
            }

            for(int i = 1; i < input + 1; i++) {
                if(input % i == 0) { // 약수이고 자기 자신이 아닌 경우 추가
                    inputList.add(i); // 약수를 inputList에 추가
                    sum += i; // 약수들의 합 저장
                }
            }

            inputList.sort(Comparator.naturalOrder()); // 오름차순 정렬

            if(sum - input == input) { // 완전수인 경우
                sb.append(input).append(" = 1");
                for(int i = 1; i < inputList.size() - 1; i++) {
                    sb.append(" + ").append(inputList.get(i));
                }
            }
            else{ // 아닌 경우
                sb.append(input).append(" is NOT perfect.");
            }

            System.out.println(sb);
        }
    }
    public static void main(String[] args) throws Exception {
        solution();
    }
}