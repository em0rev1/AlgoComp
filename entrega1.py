{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "679695ea-b54d-42cd-a489-ee98380ad663",
   "metadata": {},
   "outputs": [],
   "source": [
    "alfabeto = 'abcdefghijklmnopqrstuvwxyz'\n",
    "diccionario_posiciones = {l: posicion for posicion, l in enumerate(alfabeto)}\n",
    "k=26\n",
    "\n",
    "def letraizq(resto,i):\n",
    "    t=(k**i-1)//(k-1)\n",
    "    cociente=resto//t\n",
    "    resto = resto%t\n",
    "    letra = alfabeto[cociente]\n",
    "    return (letra,resto)\n",
    "\n",
    "def number2word(p,n):\n",
    "    s=\"\"\n",
    "    i=n\n",
    "    r=p-1\n",
    "    while i>0:\n",
    "        (letra,resto)=letraizq(r,i)\n",
    "        s+=letra\n",
    "        i+=-1\n",
    "        if resto == 0:\n",
    "            break\n",
    "        else:\n",
    "            r=resto-1\n",
    "    return s\n",
    "\n",
    "def word2number(w,n):\n",
    "    i=0\n",
    "    suma = len(w)\n",
    "    for j in w:\n",
    "        t=(k**(n-i)-1)//(k-1)\n",
    "        suma += diccionario_posiciones[j]*t\n",
    "        i+=1\n",
    "    return suma"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python 3 (ipykernel)",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.10.9"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
