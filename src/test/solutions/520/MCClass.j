.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static a(I)I
.var 0 is n I from Label0 to Label1
Label0:
	iload_0
	iconst_0
	if_icmpge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	iconst_0
	goto Label1
	goto Label2
Label3:
Label2:
	iload_0
	goto Label1
Label1:
	ireturn
.limit stack 4
.limit locals 1
.end method

.method public static b(I)I
.var 0 is n I from Label0 to Label1
Label0:
	iload_0
	iconst_0
	if_icmple Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	iconst_0
	goto Label1
	goto Label2
Label3:
Label2:
	iload_0
	goto Label1
Label1:
	ireturn
.limit stack 4
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x I from Label0 to Label1
	bipush 10
	istore_1
.var 2 is y Z from Label0 to Label1
	iconst_1
	istore_2
Label0:
	iload_2
	ifle Label3
	iload_1
	invokestatic MCClass/a(I)I
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	goto Label2
Label3:
	iload_1
	invokestatic MCClass/b(I)I
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label2:
Label1:
	return
.limit stack 2
.limit locals 3
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
