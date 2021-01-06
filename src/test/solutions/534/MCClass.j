.source MCClass.java
.class public MCClass
.super java.lang.Object

.method public static mul([[I[[I)[[I
.var 0 is a [[I from Label0 to Label1
.var 1 is b [[I from Label0 to Label1
.var 2 is c [[I from Label0 to Label1
	iconst_2
	multianewarray [[I 1
	dup
	iconst_0
	iconst_2
	newarray int
	aastore
	dup
	iconst_0
	aaload
	dup
	iconst_0
	iconst_0
	iastore
	dup
	iconst_1
	iconst_0
	iastore
	pop
	dup
	iconst_1
	iconst_2
	newarray int
	aastore
	dup
	iconst_1
	aaload
	dup
	iconst_0
	iconst_0
	iastore
	dup
	iconst_1
	iconst_0
	iastore
	pop
	astore_2
.var 3 is i I from Label0 to Label1
	iconst_0
	istore_3
.var 4 is j I from Label0 to Label1
	iconst_0
	istore 4
.var 5 is k I from Label0 to Label1
	iconst_0
	istore 5
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
	iconst_2
	if_icmpge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	iconst_0
	istore 4
	goto Label11
Label7:
	iconst_1
	iload 4
	iadd
	istore 4
Label11:
	iload 4
	iconst_2
	if_icmpge Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifle Label8
	iconst_0
	istore 5
	goto Label16
Label12:
	iconst_1
	iload 5
	iadd
	istore 5
Label16:
	iload 5
	iconst_3
	if_icmpge Label14
	iconst_1
	goto Label15
Label14:
	iconst_0
Label15:
	ifle Label13
	aload_2
	iload_3
	aaload
	iload 4
	aload_2
	iload_3
	aaload
	iload 4
	iaload
	aload_0
	iload_3
	aaload
	iload 5
	iaload
	aload_1
	iload 5
	aaload
	iload 4
	iaload
	imul
	iadd
	iastore
	goto Label12
Label13:
	goto Label7
Label8:
	goto Label2
Label3:
	aload_2
	goto Label1
Label1:
	areturn
.limit stack 15
.limit locals 6
.end method

.method public static main([Ljava/lang/String;)V
.var 0 is args [Ljava/lang/String; from Label0 to Label1
.var 1 is a [[I from Label0 to Label1
	iconst_2
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
	iconst_1
	iastore
	dup
	iconst_2
	iconst_1
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
	iconst_1
	iastore
	dup
	iconst_1
	iconst_1
	iastore
	dup
	iconst_2
	iconst_1
	iastore
	pop
	astore_1
.var 2 is b [[I from Label0 to Label1
	iconst_3
	multianewarray [[I 1
	dup
	iconst_0
	iconst_2
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
	iconst_1
	iastore
	pop
	dup
	iconst_1
	iconst_2
	newarray int
	aastore
	dup
	iconst_1
	aaload
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	iconst_1
	iastore
	pop
	dup
	iconst_2
	iconst_2
	newarray int
	aastore
	dup
	iconst_2
	aaload
	dup
	iconst_0
	iconst_1
	iastore
	dup
	iconst_1
	iconst_1
	iastore
	pop
	astore_2
.var 3 is c [[I from Label0 to Label1
	iconst_2
	multianewarray [[I 1
	dup
	iconst_0
	iconst_2
	newarray int
	aastore
	dup
	iconst_0
	aaload
	dup
	iconst_0
	iconst_0
	iastore
	dup
	iconst_1
	iconst_0
	iastore
	pop
	dup
	iconst_1
	iconst_2
	newarray int
	aastore
	dup
	iconst_1
	aaload
	dup
	iconst_0
	iconst_0
	iastore
	dup
	iconst_1
	iconst_0
	iastore
	pop
	astore_3
.var 4 is i I from Label0 to Label1
	iconst_0
	istore 4
.var 5 is j I from Label0 to Label1
	iconst_0
	istore 5
Label0:
	aload_1
	aload_2
	invokestatic MCClass/mul([[I[[I)[[I
	astore_3
	iconst_0
	istore 4
	goto Label6
Label2:
	iconst_1
	iload 4
	iadd
	istore 4
Label6:
	iload 4
	iconst_2
	if_icmpge Label4
	iconst_1
	goto Label5
Label4:
	iconst_0
Label5:
	ifle Label3
	iconst_0
	istore 5
	goto Label11
Label7:
	iconst_1
	iload 5
	iadd
	istore 5
Label11:
	iload 5
	iconst_2
	if_icmpge Label9
	iconst_1
	goto Label10
Label9:
	iconst_0
Label10:
	ifle Label8
	aload_3
	iload 4
	aaload
	iload 5
	iaload
	invokestatic io/string_of_int(I)Ljava/lang/String;
	invokestatic io/print(Ljava/lang/String;)V
	goto Label7
Label8:
	goto Label2
Label3:
Label1:
	return
.limit stack 9
.limit locals 6
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
