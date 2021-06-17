#include <iostream>
#include <stack>
using namespace std;
bool isOperator(char element) {
   switch (element) {
      case '+':
      case '-':
      case '/':
      case '*':
      return true;
   }
   return false;
}
string convertToInfix(string prefix) {
   stack<string> expression;
   int length = prefix.size();
   for (int i = length - 1; i >= 0; i--) {
      if (isOperator(prefix[i])) {
         string op1 = expression.top();
         expression.pop();
         string op2 = expression.top();
         expression.pop();
         string temp = "{"+op1+prefix[i]+op2+"}";
         expression.push(temp);
      } else {
         expression.push(string(1, prefix[i]));
      }
   }
   return expression.top();
}
int main(){
   string prefix = "-A/B*C$DE";
   cout<<"Prefix expression : "<<prefix<<endl;
   cout<<"Infix expression : " <<convertToInfix(prefix);
   return 0;
}