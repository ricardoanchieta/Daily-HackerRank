package InterviewPreparationKit;

/* Function Description

Complete the repeatedString function in the editor below.

repeatedString has the following parameter(s):

s: a string to repeat
n: the number of characters to consider
Returns

int: the frequency of a in the substring */

class Main {
    public static void main(String[] args) {
        String s = "aba";
        int n = 10;

        long x = getOcorrencias(s,n);

        System.out.println(x);
        }

        private static long getOcorrencias(String s, long n){
                
            if(!s.contains("a")){
                return 0;
            }
            if(s.length() == 1){
                return n;
            }

            long result = 0;
            int quantidadeStringDefault = 0;
            long repeticaoStringTotal = n/s.length();
            long restoString =  n%s.length();

            for(int i=0;i<s.length();i++){
                char caracter = s.charAt(i);
                if(caracter == 'a'){
                    quantidadeStringDefault++;
                };
            }

            result = repeticaoStringTotal*quantidadeStringDefault;

            if(restoString!=0){
                for(int i=0;i<restoString;i++){
                    char caracter = s.charAt(i);
                    if(caracter == 'a'){
                        result++;
                    };
                }
            }

            return (result);
        }
    }
