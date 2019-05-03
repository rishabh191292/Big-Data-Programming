#include <iostream>
#include <string>
#include<ctype.h>
#include <stdio.h>
using namespace std;
void matchstar(char Text[20], char Pattern[20], int TextLength, int PatternLength)
{
    int i,j,boolen, counter = 0;
    //char replace[20];
    if((TextLength == 0)||(PatternLength == 0))
    {
        cout<<"\n\nNo input Given\n\n";
    }
    if((Pattern[0] == '*')&&(Pattern[1] == '\0'))
    {
        cout<<"\n\nNo Match Possible\n\n";
        //exit;
    }
    else if ((Pattern[0] == '*') && (Pattern[1] != '\0'))
    {
        for(i=1;i<=PatternLength;i++)
        {
            Pattern[i-1] = Pattern[i];
        }
        if (PatternLength <= TextLength)
        {
            for(i=0;i<=PatternLength -1;i++)
            {
                if (Pattern[i] == Text[i])
                {
                    boolen = 1;
                }
                else
                {
                    boolen = 0;
                }
            }
        }
        else
        {
            for(i=0;i<=TextLength;i++)
            {
                if (Pattern[i] == Text[i])
                {
                    boolen = 1;
                }
                else
                {
                    boolen = 0;
                }
            }
        
        }
    }
    else
    {
    for(i=0;i<=TextLength;i++)
    {
        for(j=0;j<=PatternLength;j++)
        {
        if(Pattern[j] == '*')
        {
            if (Text[i] == Pattern[j-1])
            {
                counter = 1;
                //replace[i] = Text[i];
                //pos = i;
            }
            else if((counter == 1)&&(Pattern[j+1] == '\0'))
            {
                boolen = 1;
            }
            else
            {
                Pattern[j] = Pattern[j-1];
                //i = i + 1;
                //break;
            }
        }
        else if (Pattern[j] == Text[i])
        {
            boolen = 1;
        }
        else
        {
            boolen = 0;
        }
        
        }
    }
    }
    if (boolen == 1)
    {
        cout<<"\n\nA perfect match by match star function\n\n";
    }
    else
    {
        cout<<"\n\nNo match using star method\n\n";
    }
}
void matchdot(char Text[20], char Pattern[20], int TextLength, int PatternLength)
{
    int i,j,pos=0,boolen=0;
    //char replace;
    if((Pattern[0] == '.')&&(TextLength == 1))
    {
        cout<<"\n\nPerfect Match\n\n\n";
    }
    for(i=0;i<=TextLength;i++)
    {
            if((Text[i] != Pattern[i])&&(Pattern[i] == '.'))
            {
                Pattern[i] = Text[i];
                //break;
            }
    }
    if (TextLength >= PatternLength)
    {
        for(i=0;i<=PatternLength;i++)
        {
            if (Pattern[i] == Text[i])
            {
               boolen = 1;
            }
            else
            {
                boolen = 0;
            }
        }
        //cout<<"\n\n\n"<<boolen;
    }
    else
    {
        for(i=0;i<=TextLength;i++)
        {
            if (Pattern[i] == Text[i])
            {
               boolen = 1;
            }
            else
            {
                boolen = 0;
            }
        }   
    }
    if(boolen == 1)
    {
        cout<<"\n\nPerfect Match by match dot function\n\n";
    }
    else
    {
        cout<<"\n\nNo Match using dot method\n\n";
    }
}
void matchdotstar(char Text[20], char Pattern[20], int TextLength, int PatternLength)
{
    int i,j,boolen,counter=0;
    if ((Pattern[0] == '.')&&(Pattern[1] == '*')&&(PatternLength == 2))
    {
        cout<<"\n\nPerfect Match\n\n";
    }
    for(i=0;i<=PatternLength;i++)
    {
       if((Pattern[i] != isalpha(Pattern[i]))&&(Pattern[0] =='*'))
       {
           cout<<"\nNo Match Can be Found\n\n";
       }       
    }
    for(i=0;i<=TextLength;i++)
    {
        for(j=0;j<=PatternLength;j++)
        {
            if(Pattern[j] == '*')
            {
                if(Pattern[j-1] == Text[i])
                {
                    i = i+1;
                }
                else
                {
                    j = j+1;
                }
            }
            else if((Pattern[j] == '.')&&(Text[i] != Pattern[j]))
            {
                Pattern[j] = Text[i];
            }
            else if(Pattern[j] == Text[i])
            {
                counter = 1;
            }
            else
            {
                counter = 0;
            }     
        }
    }
    if(counter == 1)
    {
        cout<<"\nMatch Found by match dot star function\n";
    }
    else
    {
        cout<<"\nNo Match Found using dot star method\n";
    }
}
int main()
{
    char Text_S1[20];
    int choice;
    char Pattern_S2[20];
    int inputLengthS1,PatternLengthS2;
    cout<<"\n\nEnter the choice where \n\n 1.Pattern String with Star Only\n\n 2.Pattern String with Dot Only\n\n 3.Pattern String Having Combination of both star and dot\n\n ";
    cin>>choice;
    cout<<"\n\nEnter the length of S1\n\n";
    cin>>inputLengthS1;
    cout<<"\n\nEnter the Length of S2\n\n";
    cin>>PatternLengthS2;
    cout<<"\n\n\nEnter S1\n\n";
    for(int i=0;i<=inputLengthS1;i++)
    {
        cin>>Text_S1[i];
    }
    cout<<"\n\nEnter S2\n\n";
    for(int i=0;i<=PatternLengthS2;i++)
    {
        cin>>Pattern_S2[i];
    }
    if(choice == 1)
    {
        matchstar(Text_S1,Pattern_S2,inputLengthS1,PatternLengthS2);
    }
    else if(choice == 2)
    {
       matchdot(Text_S1,Pattern_S2,inputLengthS1,PatternLengthS2);
    }
    else if(choice == 3)
    {
        matchdotstar(Text_S1,Pattern_S2,inputLengthS1,PatternLengthS2);
    }
    else
    {
        cout<<"\n\n\nWrong Choice\n\n\n";
    }
    return 0;
}
