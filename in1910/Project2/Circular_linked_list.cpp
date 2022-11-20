
using namespace std;
#include <iostream>
#include <vector>
class CirkLinkedList
{
    struct Node
    {
        int value;
        Node *next;

        Node(int v, Node *n)
        {
            value = v;
            next = n;
        }
        Node(int v)
        {
            value = v;
            next = nullptr;
        }
    };

private:
    Node *head;

public:
    int size = 0;
    int &operator[](int index)
    {
        Node *cur = head;

        if (index > size)
        {
            throw range_error("Index out of range");
        }
        for (int i = 0; i < index; i++)
        {

            cur = cur->next;
        }
        return cur->value;
    }

    CirkLinkedList(int e)
    {
        head = nullptr;
        for (int i = 1; i <= e; i++)
        {
            append(i);
        }
    }

    void append(int val)
    {

        if (head == nullptr)
        {
            head = new Node(val);
            size++;
            return;
        }

        if (size == 1)
        {
            head->next = new Node(val);
            head->next->next = head;
            size++;
            return;
        }

        Node *cur = head;

        for (int i = 0; i < size - 1; i++)
        {
            cur = cur->next;
        }
        cur->next = new Node(val);
        cur->next->next = head;
        size++;
    }

    int pop(int index)
    {
        Node *cur = head;
        Node *temp;

        for (int i = 0; i < index; i++)
        {
            temp = cur;
            cur = cur->next;
        }
        int a = cur->value;
        temp->next = cur->next;
        size--;
        delete cur;
        //head = temp;
        return a;
    }

    vector<int> josephus_sequence(int k)
    {
        Node *dead = head;
        Node *kill = head;
        vector<int> vec;

        while (dead->next != dead)
        {
            int c = 1;
            while (c != k)
            {
                kill = dead;
                dead = dead->next;
                c++;
            }
            kill->next = dead->next;
            vec.push_back(dead->value);
            free(dead);
            //I used a long time on this task, finally finding this free function, i hope we weren't not suposed to use this.
            dead = kill->next;
        }
        //cout << b;
        vec.push_back(dead->value);
        return {vec};
    }
    void print()
    {
        Node *cur = head;

        cout << "[";
        for (int i = 1; i <= size; i++)
        {
            cout << cur->value;

            cur = cur->next;
            if (i != size)
            {
                cout << ", ";
            }
        }
        cout << "]";
    }
};

int last_man_standing(int n, int k)
{
    CirkLinkedList liste(n);
    vector<int> a = liste.josephus_sequence(k);
    int ret = 0;
    for (int e : a)
    {
        ret = e;
    }
    return ret;
}

int main()
{
    //CirkLinkedList liste(68);
    //liste.print();
    //liste.append(2);
    //liste.append(1);

    //liste.print();
    //vector<int> a = liste.josephus_sequence(7);
    //for (int e : a)
    //{
    //   cout << e << ", ";
    // }
    //cout << liste[4];

    cout << last_man_standing(68, 7);
    return 0;
}