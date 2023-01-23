package InterviewPreparationKit;

import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;

class Result {

    /*
     * Complete the 'minimumBribes' function below.
     *
     * The function accepts INTEGER_ARRAY q as parameter.
     */

    public static void minimumBribes(List<Integer> q) {
    // Write your code here
    Integer bribeGeral = 0;
    Boolean chaotic = false;

    for(int i=q.size() -1;i>=0;i--){
        if(q.get(i)!= i+1){
            if((i-1)>= 0 && q.get(i-1) == i+1){
                int aux = q.get(i-1);
                q.set((i-1),q.get(i));
                q.set(i,aux);
                bribeGeral++;
            } else if ((i-2) >= 0 && q.get(i-2) == i+1){
                q.set(i-2, q.get(i-1));
                q.set(i-1, q.get(i));
                q.set(i, q.get(i-2));
                bribeGeral +=2;
            } else {
                chaotic = true;
                break;
            }
        }
        
        
    }

    if(chaotic){
        System.out.println("Too chaotic");
    }else{
        System.out.println(bribeGeral);
    }
    
}

}
