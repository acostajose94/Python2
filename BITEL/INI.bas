Sub formateaBitel()
    ' Eliminar todo el contenido de la columna AF
    Columns("AF:AF").ClearContents

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
    ' Dim columnText As Variant
    ' Dim columnNumber As Variant
    ' Dim columnDate As Variant
    
    ' ' Definir las columnas por tipo de datos
    ' columnText = Array("B:B", "C:C", "E:E", "K:K", "AB:AB", "AE:AE")
    ' columnNumber = Array("G:G")
    ' columnDate = Array("H:H", "I:I", "L:L", "M:M", "P:P", "Q:Q", "W:W", "X:X")

    ' ' Aplicar formatos a las columnas de texto
    ' Dim textCol As Variant
    ' For Each textCol In columnText
    '     On Error Resume Next
    '     Columns(textCol).SpecialCells(xlCellTypeConstants, xlTextValues).NumberFormat = "@"
    '     On Error GoTo 0
    ' Next textCol

    ' ' Aplicar formatos a las columnas de número
    ' Dim numberCol As Variant
    ' For Each numberCol In columnNumber
    '     On Error Resume Next
    '     Columns(numberCol).SpecialCells(xlCellTypeConstants, xlNumbers).NumberFormat = "General"
    '     On Error GoTo 0
    ' Next numberCol

    ' ' Aplicar formatos a las columnas de fecha
    ' Dim dateCol As Variant
    ' For Each dateCol In columnDate
    '     On Error Resume Next
    '     Columns(dateCol).SpecialCells(xlCellTypeConstants, xlNumbers).NumberFormat = "m/d/yyyy"
    '     On Error GoTo 0
    ' Next dateCol


    Application.CutCopyMode = False ' Limpiar el portapapeles después de la operación de copiar
End Sub
