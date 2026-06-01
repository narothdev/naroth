from odoo import models, fields,api
class PurchaseOrder(models.Model):
    _inherit = "purchase.order"
    def get_line(self):
        result=[]
        for idx,line in enumerate(self.order_line,start=1):
            result.append({
                'no':idx,
                'name':line.name,
                'qty':line.product_qty,
                'unit_price':line.price_unit,
                'subtotal':line.price_subtotal,
            })
        reserve_line=max(10,len(result))
        for i in range(len(result)+1,reserve_line+1):
            result.append({
                'no':i,
                'name':'',
                'qty':'',
                'unit_price':'',
                'subtotal':''
            })
        return result

class PurchaseOrderLine(models.Model):
    _inherit = "purchase.order.line"