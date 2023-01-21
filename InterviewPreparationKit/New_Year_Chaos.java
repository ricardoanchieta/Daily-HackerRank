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
    ArrayList<Integer> aux = new ArrayList<>();
    Integer bribeGeral = 0;
    Boolean chaotic = false;
    for(int i=0;i<q.size();i++){
        aux.add(i+1);
        if(q.get(i) <= i){
            continue;
        }else{
            Integer bribeIndividual = q.get(i)- (i+1);
            if(bribeIndividual > 2 || bribeIndividual < -2){
                chaotic = true;
                break;
            }else{
                bribeGeral+= bribeIndividual;
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
