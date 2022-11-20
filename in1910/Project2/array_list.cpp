using namespace std;
#include <iostream>
#include <vector>
#include <chrono>
class ArrayList
{

private:
    int capacity;
    int *data;

    void resize()
    {
        capacity *= 2;
        int *tmp = new int[capacity];
        for (int i = 0; i < size; i++)
        {
            tmp[i] = data[i];
        }
        delete[] data;
        data = tmp;
    };
    void shrink_to_fit()
    {

        for (int i = 2; i < size * 2; i = i * i)
        {

            if (i > size)
            {
                capacity = i;
                break;
            }
        }
        int *tmp = new int[capacity];
        for (int i = 0; i < size; i++)
        {
            tmp[i] = data[i];
        }
        delete[] data;
        data = tmp;
    };

public:
    int size;
    int cap()
    {
        return capacity;
    }
    int &operator[](int i)
    {
        if (0 <= i and i < size)
        {
            return data[i];
        }
        else
        {
            throw out_of_range(("Index error"));
        }
    }
    ArrayList(vector<int> initial)
    {
        size = 0;
        capacity = 1;
        data = new int[capacity];
        for (int e : initial)
        {
            add(e);
        }
    }

    ~ArrayList()
    {
        size = 0;
        delete[] data;
    };

    void print() const
    {
        cout << "[";
        for (int i = 0; i < size; i++)
        {
            cout << data[i];
            if (i + 1 < size)
            {
                cout << ", ";
            }
        }
        cout << "]"
             << "\n";
    }

    void add(int n)
    {
        if (size >= capacity)
        {
            resize();
        }
        data[size++] = n;
    }
    void insert(int num, int index)
    {
        int a = num;
        int b = 0;
        size++;
        for (int i = index; i <= size; i++)
        {
            int b = data[i];
            data[i] = a;
            a = b;
        }
    }
    void remove(int index)
    {

        size--;

        for (int i = index; i <= size; i++)
        {
            data[i] = data[i + 1];
        }
        if (size < capacity / 4)
        {
            shrink_to_fit();
        }
    }

    int pop(int i)
    {
        int a = data[i];
        remove(i);
        return a;
    }
    void pop()
    {
        remove(size);
    }
    inline int ArrayLength() { return size; }
};

bool is_prime(int num)
{
    bool prime = true;
    if (num > 1)
    {
        for (int i = 2; i < num; i++)
        {
            if ((num % i) == 0)
            {
                prime = false;
            }
        }
    }
    return prime;
}
void add_primes(int n, ArrayList *p)
{
    int added = 0;
    int num = 1;
    while (added < n)
    {

        if (is_prime(num))
        {
            p->add(num);
            added += 1;
        }
        num += 1;
    }
}
long long int timing()
{

    ArrayList liste({0});

    //_________________________________________________________________________________________________
    //insert at end
    auto start = chrono::steady_clock::now();

    for (int i = 1; i <= 10000000; i++)
    {
        liste.add(i);
    }
    auto end = chrono::steady_clock::now();

    auto diff = end - start;
    cout << chrono::duration<double, milli>(diff).count() << " ms" << endl;
    //_________________________________________________________________________________________________
    //read from index
    int a = 0;
    start = chrono::steady_clock::now();
    for (int i = 0; i < 10000000; i = i + 1)
    {
        a = liste[i];
    }

    end = chrono::steady_clock::now();

    diff = end - start;

    cout << chrono::duration<double, milli>(diff).count() << " ms" << endl;
    //_________________________________________________________________________________________________
    //insert into beginnint
    start = chrono::steady_clock::now();

    for (int i = 0; i < 100; i = i + 1)
    {
        liste.insert(i, 0);
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
    }

    end = chrono::steady_clock::now();

    diff = end - start;

    cout << chrono::duration<double, milli>(diff).count() << " ms" << endl;
    //_________________________________________________________________________________________________
    //remove from front
    start = chrono::steady_clock::now();

    for (int i = 0; i < 100; i = i + 1)
    {
        liste.remove(0);
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
    ArrayList liste({1, 2, 3, 4, 5});
    liste.print();
    cout << "element in index 2 = " << liste[2] << "\n";
    liste.pop();
    liste.print();
    cout << liste.pop(0) << "\n";
    liste.add(100);
    liste.print();
    liste.pop();
    liste.print();
    cout << "length = " << liste.ArrayLength() << "\n";
    liste.insert(50, 0);
    liste.print();

    //timing();
    return 0;
};
