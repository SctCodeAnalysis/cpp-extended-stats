class J {};

class A {};

class B : public A {};

class C : public B, private J {};

class D : public B {};

class E : public C {};

class F : public D {};

class G : public C, public D {};

class H : public E, public F {};

class I : public G, public H {};

class K : public J {};

class L : public K {};
