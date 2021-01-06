.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static findMax([II)I
.var 0 is a [I from Label0 to Label1
.var 1 is i I from Label0 to Label1
.var 2 is x I from Label0 to Label1
	iconst_0
	istore_2
Label0:
	aload_0
	iload_1
	iaload
	istore_2
	iload_1
	bipush 9
	if_icmpne Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	iload_2
	goto Label1
	goto Label2
Label3:
.var 3 is y I from Label0 to Label1
	iconst_0
	istore_3
	aload_0
	iload_1
	iconst_1
	iadd
	invokestatic MCClass/findMax([II)I
	istore_3
	iload_2
	iload_3
	if_icmple Label8
	iconst_1
	goto Label9
Label8:
	iconst_0
Label9:
	ifle Label7
	iload_2
	goto Label1
	goto Label6
Label7:
	iload_3
	goto Label1
Label6:
Label2:
Label1:
	ireturn
.limit stack 7
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is i I from Label0 to Label1
	iconst_0
	istore_1
.var 2 is a [I from Label0 to Label1
	bipush 10
	newarray int
	dup
	iconst_0
	iconst_2
	iastore
	dup
	iconst_1
	iconst_4
	iastore
	dup
	iconst_2
	bipush 6
	iastore
	dup
	iconst_3
	bipush 8
	iastore
	dup
	iconst_4
	iconst_1
	iastore
	dup
	iconst_5
	iconst_3
	iastore
	dup
	bipush 6
	iconst_5
	iastore
	dup
	bipush 7
	bipush 7
	iastore
	dup
	bipush 8
	bipush 9
	iastore
	dup
	bipush 9
	iconst_0
	iastore
	astore_2
.var 3 is x I from Label0 to Label1
	iconst_0
	istore_3
Label0:
	aload_2
	iload_1
	invokestatic MCClass/findMax([II)I
	istore_3
	iload_3
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 4
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
