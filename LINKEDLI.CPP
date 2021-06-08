#include<iostream.h>
#include<conio.h>
#include<iomanip.h>
#define NULL 0
struct node
{
int info;
node *link;
};
int main()
{
node* create();
void traverse(node*);
node* search(node*,int);
void instloc(node**,int,node*);
clrscr();
node *head=create();
int item;
cout<<" \n enter item to search from linked list:";
cin>>item;
node *loc=search(head,item);
cout<<"linked list before insertion \n";
traverse(head);
int data;
cout<<"\n enter info to be inserted into new node=";
cin>>data;
instloc(&head,data,loc);
cout<<"linked list afterinsertion \n";
traverse(head);
cout<<"\n end of the program----------\n";
node *ptr=head;
while(ptr!=NULL)
{
  ptr=ptr->link;
  delete head;
  head=ptr;
}
getch();
return 0;
}
node* create()
{
node *ptr,*head=NULL;
char ch='y';
while (ch=='y'|| ch=='Y')
{
if(head==NULL)
{
head= new node;
ptr=head;
}
else
{
ptr->link=new node;
ptr=ptr->link;
}
int data;
cout<<"enter info of new node\t=";
cin>>data;
ptr->info=data;
cout.flush();
cout<<"want to continue :(Y or N)=\n";
cin>>ch;
}
ptr->link=NULL;
return(head);
}
void traverse(node *head)
{
node *ptr=head;
while (ptr!=NULL)
{
cout<<"\n info of node is \t="<<ptr ->info;
ptr=ptr->link;
}
return;
}
node* search(node *head,int item)
{
node *loc,*ptr;
loc=NULL;
ptr=head;
while ( (ptr!=NULL) && (item!=ptr->info) )
ptr=ptr->link;
if(item==ptr->info)
loc=ptr;
return(loc);
}
void instloc(node** head,int item,node *loc)
{
node* newnode;
newnode= new node;
newnode->info=item;
if(loc==NULL)
{
 newnode->link=*head;
 *head=newnode;
}
else
{
newnode->link=loc->link;
loc->link=newnode;
}
}
