.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static inc(I)I
.var 0 is n I from Label0 to Label1
Label0:
	iload_0
	iconst_1
	iadd
	goto Label1
Label1:
	ireturn
.limit stack 2
.limit locals 1
.end method

.method public static dub(I)I
.var 0 is n I from Label0 to Label1
Label0:
	iconst_2
	iload_0
	imul
	goto Label1
Label1:
	ireturn
.limit stack 2
.limit locals 1
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is x I from Label0 to Label1
	iconst_3
	istore_1
.var 2 is a I from Label0 to Label1
	iconst_0
	istore_2
.var 3 is b I from Label0 to Label1
	iconst_0
	istore_3
Label0:
	iload_1
	invokestatic MCClass/dub(I)I
	invokestatic MCClass/inc(I)I
	istore_2
	iload_1
	invokestatic MCClass/inc(I)I
	invokestatic MCClass/dub(I)I
	istore_3
	iload_2
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	iload_3
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 1
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
