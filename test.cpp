#include <iostream>
#include <string>
using namespace std;
void abc(char string1[], char string2[], int str1, int str2)
{
    int i, j,position1 = -1,position2 = -1;
    string lcs1,lcs2;
    if (string1 == NULL || string2 == NULL)
    {
        cout<<"\n\n Invalid Condition";
    }
    for(i=0 ; i<= str1 ; i++)
    {
        
        for(j=position1 ; j<= str2 ;j++)
        {
            
            if(string1[i] == string2[j])
            {
                //cout<<"\n"<<string1[i];
                lcs1 = lcs1 + string1[i];
                position1 = j+1;
                break;
            }
            
        }
    }
    for(i=0 ; i<= str2 ; i++)
    {
        
        for(j=position2 ; j<= str1 ;j++)
        {
            
            if(string2[i] == string1[j])
            {
                //cout<<"\n"<<string2[i];
                lcs2 = lcs2 + string2[i];
                position2 = j+1;
                break;
            }
            
        }
    }
    //cout<<"\n"<<lcs1<<"\n\n";
    //cout<<"\n"<<lcs2<<"\n\n";

    if(lcs1.size() > lcs2.size())
    {
        cout<<"\n\nThe longest subsequence is\n\n"<<lcs1<<"\n\n\n";
    }
    else
    {
        cout<<"\n\nThe Longest subsequence is\n\n"<<lcs2<<"\n\n";
    }

}
int main()
{
    char str1[20];
    char str2[20];
    int strlen1, strlen2;
    cout<<"\nEnter the strings one\n";
    cin>>str1;
    cout<<"\nEnter the string two\n";
    cin>>str2;
    strlen1 = strlen(str1);
    strlen2 = strlen(str2);
    abc(str1, str2, strlen1, strlen2);
    return 0;
}