' Crear una función en VB que valide el formato del RUT chileno
Function ValidarRUT(rut As String) As Boolean
    ' Eliminar puntos y guiones
    rut = rut.Replace(".", "").Replace("-", "").ToUpper()

    ' Verificar que el RUT tenga al menos 2 caracteres (número y dígito verificador)
    If rut.Length < 2 Then
        Return False
    End If

    ' Separar el número y el dígito verificador
    Dim numero As String = rut.Substring(0, rut.Length - 1)
    Dim dv As Char = rut(rut.Length - 1)

    ' Calcular el dígito verificador esperado
    Dim suma As Integer = 0
    Dim multiplicador As Integer = 2

    For i As Integer = numero.Length - 1 To 0 Step -1
        suma += CInt(numero(i).ToString()) * multiplicador
        multiplicador += 1
        If multiplicador > 7 Then
            multiplicador = 2
        End If
    Next

    Dim resto As Integer = suma Mod 11
    Dim dvEsperado As Char

    If resto = 1 Then
        dvEsperado = "K"c
    ElseIf resto = 0 Then
        dvEsperado = "0"c
    Else
        dvEsperado = CChar((11 - resto).ToString())
    End If

    ' Comparar el dígito verificador calculado con el proporcionado
    Return dvEsperado = dv
End Function
