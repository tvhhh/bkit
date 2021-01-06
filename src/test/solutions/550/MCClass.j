.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static a [I
.field static x I

.method public static count([II)I
.var 0 is a [I from Label0 to Label1
.var 1 is x I from Label0 to Label1
.var 2 is c I from Label0 to Label1
	iconst_0
	istore_2
.var 3 is i I from Label0 to Label1
	iconst_0
	istore_3
Label0:
	iconst_0
	istore_3
	goto Label6
Label2:
	iconst_1
	iload_3
	iadd
	istore_3
Label6:
	iload_3
	bipush 10
	if_icmpge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	aload_0
	iload_3
	iaload
	iload_1
	if_icmpne Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifle Label8
	iload_2
	iconst_1
	iadd
	istore_2
	goto Label7
Label8:
Label7:
	goto Label2
Label3:
	iload_2
	goto Label1
Label1:
	ireturn
.limit stack 7
.limit locals 4
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
	bipush 10
	newarray int
	dup
	iconst_0
	iconst_2
	iastore
	dup
	iconst_1
	iconst_1
	iastore
	dup
	iconst_2
	iconst_2
	iastore
	dup
	iconst_3
	iconst_3
	iastore
	dup
	iconst_4
	iconst_4
	iastore
	dup
	iconst_5
	iconst_4
	iastore
	dup
	bipush 6
	iconst_3
	iastore
	dup
	bipush 7
	iconst_4
	iastore
	dup
	bipush 8
	iconst_3
	iastore
	dup
	bipush 9
	iconst_3
	iastore
	putstatic MCClass.a [I
	iconst_3
	putstatic MCClass.x I
.var 1 is c I from Label0 to Label1
	iconst_4
	istore_1
Label0:
	getstatic MCClass.a [I
	iload_1
	invokestatic MCClass/count([II)I
	istore_1
	iload_1
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
Label1:
	return
.limit stack 4
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
