
using namespace std;
#include <iostream>
#include <vector>
#include <chrono>
class LinkedList
{
    struct Node
    {
        int value;
        Node *prev;
        Node *next;
        Node(int v, Node *p, Node *n)
        {
            value = v;
            prev = p;
            next = n;
        }
        Node(int v, Node *p)
        {
            value = v;
            prev = p;
            next = nullptr;
        }
        Node(int v)
        {
            value = v;
            next = nullptr;
            prev = nullptr;
        }
    };

private:
    Node *head;
    Node *tail;

public:
    int &operator[](int index)
    {
        Node *cur = head;

        for (int i = 0; i < index; i++)
        {
            if (cur->next != nullptr)
            {
                cur = cur->next;
            }
            else
            {
                throw range_error("Index out of range");
            }
        }
        return cur->value;
    }

    LinkedList(vector<int> initial)
    {
        head = nullptr;
        tail = nullptr;
        for (int e : initial)
        {
            append(e);
        }
    }

    int length()
    {
        Node *cur = head;
        int c = 0;

        while (cur != nullptr)
        {
            c++;
            cur = cur->next;
        }

        return c;
    }
    ~LinkedList()
    {
        Node *cur;
        Node *ny;

        cur = head;

        while (cur != nullptr)
        {
            ny = cur->next;
            cur->next = nullptr;
            cur->prev = nullptr;
            delete cur;
            cur = ny;
        }
    }

    void append(int val)
    {

        if (head == nullptr)
        {
            head = new Node(val);
            return;
        }
        if (tail == nullptr)
        {
            head->next = new Node(val, head);
            tail = head->next;
            return;
        }

        tail->next = new Node(val, tail);
        tail = tail->next;
    }
    void insert(int val, int index)
    {
        Node *cur = head;

        for (int i = 0; i < index; i++)
        {
            if (cur->next != nullptr)
            {
                cur = cur->next;
            }
            else
            {
                throw range_error("Index out of range");
            }
        }

        Node *node = new Node(val, cur->prev, cur);
        cur->prev->next = node;
        cur->prev = node;
    }

    void remove(int index)
    {
        Node *cur = head;

        for (int i = 0; i < index; i++)
        {
            if (cur->next != nullptr)
            {
                cur = cur->next;
            }
            else
            {
                throw range_error("Index out of range");
            }
        }

        cur->prev->next = cur->next;
        cur->next->prev = cur->prev;
        delete cur;
    }
    int pop(int index)
    {
        Node *cur = head;

        for (int i = 0; i < index; i++)
        {
            if (cur->next != nullptr)
            {
                cur = cur->next;
            }
            else
            {
                throw range_error("Index out of range");
            }
        }

        cur->prev->next = cur->next;
        cur->next->prev = cur->prev;
        int a = cur->value;
        delete cur;
        return a;
    }
    void pop()
    {
        Node *cur = tail;
        tail = cur->prev;
        tail->next = nullptr;
        delete cur;
    }
    void print()
    {
        Node *cur = head;

        cout << "[";
        while (cur != nullptr)
        {
            cout << cur->value;

            cur = cur->next;
            if (cur != nullptr)
            {
                cout << ", ";
            }
        }
        cout << "]";
    }
};
int timing()
{

    LinkedList liste({0});

    //_________________________________________________________________________________________________
    //insert at end
    auto start = chrono::steady_clock::now();

    for (int i = 1; i <= 10000000; i++)
    {
        liste.append(i);
    }
    auto end = chrono::steady_clock::now();

    auto diff = end - start;
    cout << chrono::duration<double, milli>(diff).count() << " ms" << endl;
    //_________________________________________________________________________________________________
    //read from index
    int a = 0;
    start = chrono::steady_clock::now();
    for (int i = 0; i < 10000; i = i + 1)
    {
        a = liste[i];
        i = i;
    }

    end = chrono::steady_clock::now();

    diff = end - start;

    cout << chrono::duration<double, milli>(diff).count() << " ms" << endl;
    //_________________________________________________________________________________________________
    //insert into beginning
    start = chrono::steady_clock::now();

    for (int i = 0; i < 1000000; i = i + 1)
    {
        liste.insert(i, 1);
        i = i;
    }

    end = chrono::steady_clock::now();

    diff = end - start;

    cout << chrono::duration<double, milli>(diff).count() << " ms" << endl;
    //_________________________________________________________________________________________________
    //insert into middle
    start = chrono::steady_clock::now();

    for (int i = 0; i < 100; i = i + 1)
    {
        liste.insert(i, 5000000);
        i = i;
    }

    end = chrono::steady_clock::now();

    diff = end - start;

    cout << chrono::duration<double, milli>(diff).count() << " ms" << endl;
    //_________________________________________________________________________________________________
    //remove from front
    start = chrono::steady_clock::now();

    for (int i = 0; i < 1000000; i = i + 1)
    {
        liste.remove(1);
        i = i;
    }

    end = chrono::steady_clock::now();

    diff = end - start;

    cout << chrono::duration<double, milli>(diff).count() << " ms" << endl;

    //_________________________________________________________________________________________________
    //remove from middle
    start = chrono::steady_clock::now();

    for (int i = 0; i < 100; i = i + 1)
    {
        liste.remove(5000000);
    }

    end = chrono::steady_clock::now();

    diff = end - start;

    cout << chrono::duration<double, milli>(diff).count() << " ms" << endl;

    //_________________________________________________________________________________________________
    //remove from back
    start = chrono::steady_clock::now();

    for (int i = 0; i < 1000000; i = i + 1)
    {
        liste.pop();
    }

    end = chrono::steady_clock::now();

    diff = end - start;

    cout << chrono::duration<double, milli>(diff).count() << " ms" << endl;
    return 0;
}
int main()
{

    LinkedList *list = new LinkedList({1, 2, 3, 4, 5});
    list->print();
    cout << "\n";
    delete list;
    //This doesnt delete completely, some bugfinding left here
    cout << "\n";
    list->print();

    LinkedList liste({2, 3, 1, 2, 1});
    liste.append(2);
    liste.append(1);
    cout << liste[2] << "\n";
    liste.print();
    liste.insert(100, 2);
    cout << "\n";
    liste.print();
    cout << "\n"
         << liste.pop(2) << "\n";
    liste.print();
    cout << "\n";
    liste.remove(2);
    liste.print();
    cout << "\n";
    liste.pop();
    liste.print();
    cout << "\n"
        //      << liste.length();

        timing();
    return 0;
};