.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x Ljava/lang/String; from Label0 to Label1
	ldc "1.0"
	astore_1
.var 2 is y F from Label0 to Label1
	ldc 1.5
	fstore_2
.var 3 is z F from Label0 to Label1
	ldc 4.5
	fstore_3
Label0:
Label2:
	fload_2
	fload_3
	fcmpl
	iconst_0
	if_icmpeq Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	fload_2
	aload_1
	invokestatic io/float_of_string(Ljava/lang/String;)F
	fadd
	fstore_2
	goto Label2
Label3:
	ldc "Hello"
	astore_1
	fload_2
	invokestatic io/string_of_float(F)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	aload_1
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 6
.limit locals 4
.end method

.method public <init>()V
.var 0 is this LMCClass; from Label0 to Label1
Label0:
	aload_0
	invokespecial java/lang/Object/<init>()V
Label1:
	return
.limit stack 1
.limit locals 1
.end method
