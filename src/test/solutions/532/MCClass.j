.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a [[I from Label0 to Label1
	iconst_3
	multianewarray [[I 1
	dup
	iconst_0
	iconst_3
	newarray int
	aastore
	dup
	iconst_0
	aaload
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
	pop
	dup
	iconst_1
	iconst_3
	newarray int
	aastore
	dup
	iconst_1
	aaload
	dup
	iconst_0
	iconst_4
	iastore
	dup
	iconst_1
	iconst_5
	iastore
	dup
	iconst_2
	bipush 6
	iastore
	pop
	dup
	iconst_2
	iconst_3
	newarray int
	aastore
	dup
	iconst_2
	aaload
	dup
	iconst_0
	bipush 7
	iastore
	dup
	iconst_1
	bipush 8
	iastore
	dup
	iconst_2
	bipush 9
	iastore
	pop
	astore_1
.var 2 is i I from Label0 to Label1
	iconst_0
	istore_2
.var 3 is j I from Label0 to Label1
	iconst_0
	istore_3
Label0:
	iconst_0
	istore_2
	goto Label6
Label2:
	iconst_1
	iload_2
	iadd
	istore_2
Label6:
	iload_2
	iconst_3
	if_icmpge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	iconst_0
	istore_3
	goto Label11
Label7:
	iconst_1
	iload_3
	iadd
	istore_3
Label11:
	iload_3
	iload_2
	if_icmpge Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifle Label8
.var 4 is tmp I from Label0 to Label1
	iconst_0
	istore 4
	aload_1
	iload_2
	aaload
	iload_3
	iaload
	istore 4
	aload_1
	iload_2
	aaload
	iload_3
	aload_1
	iload_3
	aaload
	iload_2
	iaload
	iastore
	aload_1
	iload_3
	aaload
	iload_2
	iload 4
	iastore
	goto Label7
Label8:
	goto Label2
Label3:
	iconst_0
	istore_2
	goto Label16
Label12:
	iconst_1
	iload_2
	iadd
	istore_2
Label16:
	iload_2
	iconst_3
	if_icmpge Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label13
	iconst_0
	istore_3
	goto Label21
Label17:
	iconst_1
	iload_3
	iadd
	istore_3
Label21:
	iload_3
	iconst_3
	if_icmpge Label19
	iconst_1
	goto Label20
Label19:
	iconst_0
Label20:
	ifle Label18
	aload_1
	iload_2
	aaload
	iload_3
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	goto Label17
Label18:
	goto Label12
Label13:
Label1:
	return
.limit stack 15
.limit locals 5
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
