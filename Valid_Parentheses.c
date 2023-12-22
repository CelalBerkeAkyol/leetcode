char Stack[1000];
int top = -1; // stack boş

void push(char s)
{
    top++;
    Stack[top] = s;
}

char pop()
{
    if (top == -1)
        return (0);
    char deletedVal = Stack[top];
    top--;
    return deletedVal;
}

// kontrol fonksiyonu
bool isValid(char *s)
{
    int dogruMu = 1; // bu değeri doğruluğu kontrol etmek için kullanacağım
    int count = 0; 
    int lenghtS = 0; 

    // hiç bir eleman yoksa true döndür
    if (s[0] == '\0')
        return true;
    
    // kapama değeri ile başlıyorsa false döndür
    if (s[0] == ')' || s[0] == '}' || s[0] == ']')
        return false;
    
    // s dizisindeki tüm değerleri kontrol et
    for (int i = 0; s[i] != '\0'; ++i)
    {
        lenghtS ++;
        // eğer açma değerleri varsa stacke depola
        if (s[i] == '(' || s[i] == '{' || s[i] == '[')
        {
            push(s[i]);
            continue;
        }

        // kapama değerleri gelirse stacktan son elemanı çıkar ve şu anki karakter ile karşılaştır
        else if (s[i] == ')' || s[i] == '}' || s[i] == ']')
        {
            char deletedVal = pop();
            count++; // kapama yoksa hata verdirtmek için var 
            if (deletedVal == '(' && s[i] == ')')
                continue;
            else if (deletedVal == '{' && s[i] == '}')
                continue;
            else if (deletedVal == '[' && s[i] == ']')
                continue;
            else
            {
                dogruMu = 0;
                return false;
            }
        }
        // yukarıdaki else bloğu hiç çalışmazsa doğruMu değişkenin değeri hala 1 olur demekki stack boşalana kadar istenmeyen bir durum olmamıştır
    }
    if(count == 0)
        return false;
    else if(lenghtS %2 == 1)
        return false;
    else if (dogruMu == 1)
        return true;
        else
    return false;
}
