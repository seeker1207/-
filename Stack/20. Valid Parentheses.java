class Solution {
    public boolean isValid(String s) {
        Stack<String> stack = new Stack<>();
        Map<String, String> parenMap = new HashMap<>();
        parenMap.put(")", "(");
        parenMap.put("]", "[");
        parenMap.put("}", "{");


        for (String ch : s.split("")) {
            if (stack.size() != 0 && parenMap.containsKey(ch) && 
                    parenMap.get(ch).equals(stack.peek())) {
                stack.pop();
                continue;
            }
            stack.push(ch);
            // System.out.println(stack);
        }

        return stack.size() == 0;
    }
}
