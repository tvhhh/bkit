.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static foo(I)Ljava/lang/String;
.var 0 is n I from Label0 to Label1
Label0:
	iload_0
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	iload_0
	iconst_0
	if_icmple Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	iload_0
	iconst_1
	isub
	invokestatic MCClass/foo(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	goto Label2
Label3:
Label2:
	iload_0
	invokestatic io/string_of_int(I)Ljava/lang/String;
	goto Label1
Label1:
	areturn
.limit stack 4
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x Ljava/lang/String; from Label0 to Label1
	ldc ""
	astore_1
Label0:
	iconst_5
	invokestatic MCClass/foo(I)Ljava/lang/String;
	astore_1
Label1:
	return
.limit stack 1
.limit locals 2
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
