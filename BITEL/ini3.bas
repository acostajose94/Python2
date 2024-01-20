Sub formateaBitel()

    ' Crear una nueva hoja llamada "AGRUPADO"
    Dim agrupadoSheet As Worksheet
    Set agrupadoSheet = Worksheets.Add
    agrupadoSheet.Name = "AGRUPADO"

    Dim ws As Worksheet
    On Error Resume Next
    Set ws = Worksheets("Despues")
    On Error GoTo 0

    If Not ws Is Nothing Then
        Dim lastRowDespues As Long
        lastRowDespues = ws.Cells(ws.Rows.Count, "AB").End(xlUp).Row
        ws.Range("AB1:AB" & lastRowDespues).Copy
        ws.Range("AD1").PasteSpecial Paste:=xlPasteValues
        Application.CutCopyMode = False

        ' Copiar todo el contenido de "Despues" a "AGRUPADO", excepto la primera fila
        Dim lastRowAgrupado As Long
        lastRowAgrupado = agrupadoSheet.Cells(agrupadoSheet.Rows.Count, "A").End(xlUp).Row
        ws.Range("A2:AB" & lastRowDespues).Copy Destination:=agrupadoSheet.Range("A" & lastRowAgrupado + 1)
        Application.CutCopyMode = False
    End If

    ' Copiar los datos de "Antes" sin cabecera debajo de los datos de "Despues" en la hoja "AGRUPADO"
    Dim antesSheet As Worksheet
    On Error Resume Next
    Set antesSheet = Worksheets("Antes")
    On Error GoTo 0

    If Not antesSheet Is Nothing Then
        Dim lastRowAntes As Long
        lastRowAntes = antesSheet.Cells(antesSheet.Rows.Count, "A").End(xlUp).Row

        ' Pegar los datos de "Antes" sin cabecera debajo de los datos de "Despues" en la hoja "AGRUPADO"
        Dim lastRowAgrupadoDespues As Long
        lastRowAgrupadoDespues = agrupadoSheet.Cells(agrupadoSheet.Rows.Count, "A").End(xlUp).Row

        antesSheet.Range("A2:AB" & lastRowAntes).Copy
        agrupadoSheet.Range("A" & lastRowAgrupadoDespues + 1).PasteSpecial Paste:=xlPasteValues
        Application.CutCopyMode = False
    End If

    ' Eliminar todo el contenido de la columna AF
    Columns("AF:AF").ClearContents

    ' Copiar el contenido de la hoja actual desde la columna A hasta la columna AH
    ' Copiar el contenido de la hoja actual desde la columna A hasta la columna AH
    Dim lastRow As Long
    lastRow = Cells(Rows.Count, "A").End(xlUp).Row
    Range("A1:AH" & lastRow).Copy

    ' Crear una nueva hoja llamada "TOTAL" y pegar el contenido copiado en A1
    Dim newSheet As Worksheet
    Set newSheet = Worksheets.Add
    newSheet.Name = "TOTAL"
    newSheet.Range("A1").PasteSpecial Paste:=xlPasteValues
    ' Insertar una columna vacía en la columna B en la hoja actual
    Sheets("TOTAL").Columns("AF:AF").Insert Shift:=xlToRight, CopyOrigin:=xlFormatFromLeftOrAbove

    ' Calcular el total de cada fila en la columna B de la ho
    Dim valuesArray As Variant
    valuesArray = Array("PROMOTION_CODE", "SUB_ID", "ISDN", "PRODUCT_CODE", "BILL_CYCLE", "INVOICE_NUMBER", _
                                   "AMOUNT", "DATE_EXPORT_INVOICE", "DATE_EXPIRED_INVOICE", "DAY_OVERDUE", "CONTRACT_ID", _
                                   "TIME_BARRING", "BILL_CYLE_DEBT", "REGISTER_STATUS", "PROMOTION_ID", "START_PROMOTION_DATE", _
                                   "END_PROMOTION_DATE", "PROCESS_STATUS", "PROCESS_DATE", "USER_PROCESS", "STATUS", _
                                   "DESCRIPTION", "START_DATE", "END_DATE", "BRANCH_CODE", "SHOP_CODE", "ID_TYPE", _
                                   "ID_NO", "FULL_NAME", "EMAIL", "TEL_FAX", "PAYMENT_DATE", "PAYMENT_STATUS", _
                                   "STATUS_LINE", "BLOCK_LINE")
    Dim i As Integer
    For i = LBound(valuesArray) To UBound(valuesArray)
        If Len(valuesArray(i)) > 0 Then
            newSheet.Cells(1, i + 1).Value = valuesArray(i)
        Else
            newSheet.Cells(1, i + 1).Value = ""
        End If
    Next i
    
    Dim columnText As Variant
    Dim columnNumber As Variant
    Dim columnDate As Variant
    
    ' Definir las columnas por tipo de datos
    columnText = Array("B:B", "C:C", "E:E", "K:K", "AB:AB", "AE:AE")
    columnNumber = Array("G:G")
    columnDate = Array("H:H", "I:I", "L:L", "M:M", "P:P", "Q:Q", "W:W", "X:X")

    
    ' Limpiar el portapapeles después de todas las operaciones de copiar
    Application.CutCopyMode = False
    ' Formatear las columnas según el tipo de datos
    FormatColumns Sheets("TOTAL"), columnText, columnNumber, columnDate
End Sub

Sub FormatColumns(ws As Worksheet, targetSheet As Worksheet, columnText As Variant, columnNumber As Variant, columnDate As Variant)
    ' Format text columns
    For Each col In columnText
        targetSheet.Columns(col).NumberFormat = "@" ' You can change the format as needed
    Next col

    ' Format number columns
    For Each col In columnNumber
        targetSheet.Columns(col).NumberFormat = "0" ' You can change the format as needed
    Next col

    ' Format date columns
    For Each col In columnDate
        targetSheet.Columns(col).NumberFormat = "yyyy-mm-dd" ' You can change the format as needed
    Next col
End Sub

