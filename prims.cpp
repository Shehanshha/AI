#include<iostream>
#define ROW 10
#define COL 10
#define infi 999
using namespace std;
class prims
{
    int graph[ROW][COL],nodes;
    public:
    void create_graph();
    void primsAlgo();
};
void prims :: create_graph()
{
    int i,j;
    cout<<"Enter the total offices:"<<endl;
    cin>>nodes;
    cout<<"Enter Adjacency Matrix:"<<endl;
    for(i=0;i<nodes;i++)
    {
        for(j=i;j<nodes;j++)
        {
            cout<<"Enter distance between "<< i<< "and "<< j<<endl;
            cin>>graph[i][j];
            graph[j][i] = graph[i][j];
        }
    }
    for(i=0;i<nodes;i++)
    {
        for(j=0;j<nodes;j++)
        {
            if(graph[i][j] == 0)
                graph[i][j] = infi;
        }
    }
}
void prims :: primsAlgo()
{
    int selected[ROW],i,j,ne=0;
    int zero = 0,one = 1,min =0,x,y;
    int cost=0;
    for(i=0;i<nodes;i++)
        selected[i] = zero;
    selected[0] = one;
    while(ne < nodes-1)
    {
        min = infi;
        for(i=0;i<nodes;i++)
        {
            if(selected[i] == one)
            {
                for(j=0;j<nodes;j++)
                {
                    if(selected[j] == zero)
                    {
                        if(min>graph[i][j])
                        {
                            min = graph[i][j];
                            x = i;
                            y = j;
                        }
                    }
                }
            }
        }
        selected[y] = one;
        cout<<"\n"
            <<x<<"-->"<<y;
        cost +=graph[x][y];
        ne++;    
    }
    cout<<"\ntotal cost is:"<<cost;
}
int main(){
    prims obj;
    obj.create_graph();
    obj.primsAlgo();
    return 0;
}