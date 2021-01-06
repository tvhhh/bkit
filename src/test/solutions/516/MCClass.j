.source MCClass.java
.class public MCClass
.super java.lang.Object
.field static x I
.field static a [I

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
	iconst_3
	putstatic MCClass.x I
	iconst_5
	newarray int
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	iconst_2
	iastore
	dup
	iconst_2
	iconst_3
	iastore
	dup
	iconst_3
	iconst_4
	iastore
	dup
	iconst_4
	iconst_5
	iastore
	putstatic MCClass.a [I
.var 1 is i I from Label0 to Label1
	iconst_0
	istore_1
Label0:
	iconst_0
	istore_1
	goto Label6
Label2:
	iconst_1
	iload_1
	iadd
	istore_1
Label6:
	iload_1
	iconst_5
	if_icmpge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	getstatic MCClass.a [I
	iload_1
	iaload
	getstatic MCClass.x I
	if_icmpne Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifle Label8
	ldc "1"
	invokestatic io/print(Ljava/lang/String;)V
	goto Label7
Label8:
	ldc "0"
	invokestatic io/print(Ljava/lang/String;)V
Label7:
	goto Label2
Label3:
Label1:
	return
.limit stack 6
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
