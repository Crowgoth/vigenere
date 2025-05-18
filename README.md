# Python practice - Vigenère cipher

Here is the [Wikipedia-Link Vigenère cipher](https://en.wikipedia.org/wiki/Vigen%C3%A8re_cipher)

This is a practice project for learning Python and git/ github. It possibly includes string manipulations, handling of list and lists of lists, functions. Also to edit this file in Markdown. There are surely a lot of ways to program such a project, this is just one example, possibly not the shortest or easiest solution.

-----

**The assignment:**

The goal is to write a program to encrypt and decrypt messages with the Vigenère cipher. There are certain points to keep in mind:
- Since you can only encrypt/ decrypt alphabetical characters with the Vigenère-array, the cleartext should be cleaned up from any non-alphabetical characters. Also, convert all the characters into uppcercase characters. 
- Since the keyword/ keyphrase to use during the encryption should be individual, the program should ask for the keyword/ keyphrase. For the encryption/ decryption process, the keyword need to be as long as the message. So the keyword maybe needs to be repeated, until it reaches the length of the message.
- The same Vigenère-array is needed for encrpytion and decryption, it might be an idea to set it as a global variable.

Example:
```
-----------------------------------------
             Vigenȩre cipher
-----------------------------------------

ABCDEFGHIJKLMNOPQRSTUVWXYZ
BCDEFGHIJKLMNOPQRSTUVWXYZA
CDEFGHIJKLMNOPQRSTUVWXYZAB
DEFGHIJKLMNOPQRSTUVWXYZABC
EFGHIJKLMNOPQRSTUVWXYZABCD
FGHIJKLMNOPQRSTUVWXYZABCDE
GHIJKLMNOPQRSTUVWXYZABCDEF
HIJKLMNOPQRSTUVWXYZABCDEFG
IJKLMNOPQRSTUVWXYZABCDEFGH
JKLMNOPQRSTUVWXYZABCDEFGHI
KLMNOPQRSTUVWXYZABCDEFGHIJ
LMNOPQRSTUVWXYZABCDEFGHIJK
MNOPQRSTUVWXYZABCDEFGHIJKL
NOPQRSTUVWXYZABCDEFGHIJKLM
OPQRSTUVWXYZABCDEFGHIJKLMN
PQRSTUVWXYZABCDEFGHIJKLMNO
QRSTUVWXYZABCDEFGHIJKLMNOP
RSTUVWXYZABCDEFGHIJKLMNOPQ
STUVWXYZABCDEFGHIJKLMNOPQR
TUVWXYZABCDEFGHIJKLMNOPQRS
UVWXYZABCDEFGHIJKLMNOPQRST
VWXYZABCDEFGHIJKLMNOPQRSTU
WXYZABCDEFGHIJKLMNOPQRSTUV
XYZABCDEFGHIJKLMNOPQRSTUVW
YZABCDEFGHIJKLMNOPQRSTUVWX
ZABCDEFGHIJKLMNOPQRSTUVWXY


Do you want to (e)ncrypt of (d)ecrypt a message? e

Please enter the String that should be used as a key: Secretkey
Please enter your message now: Weather is good, attack at dawn.


Cleaned key:       SECRETKEYSECRETKEYSECRETK
Cleaned message:   WEATHERISGOODATTACKATDAWN
===================
Processed message: OICKLXBMQYSQUEMDEACEVUEPX
```
