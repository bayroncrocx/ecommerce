from django.shortcuts import render
from django.http import HttpResponse
from collections import OrderedDict
from category.models import Category 
from orders.models import Order 

# Include the `fusioncharts.py` file that contains functions to embed the charts.
from .fusioncharts import FusionCharts

def myFirstChart(request):
# Chart data is passed to the `dataSource` parameter, like a dictionary in the form of key-value pairs.
  dataSource = OrderedDict()

# The `chartConfig` dict contains key-value pairs of data for chart attribute
  chartConfig = OrderedDict()
  chartConfig["caption"] = "Reportes de Ventas"
  chartConfig["subCaption"] = ""
  chartConfig["xAxisName"] = "Mes"
  chartConfig["yAxisName"] = "Total de ventas (Miles de pesos)"
  chartConfig["numberSuffix"] = "K"
  chartConfig["theme"] = "fusion"

  dataSource["chart"] = chartConfig
  dataSource["data"] = []

  year = "2022"
#   categories = Category.objects.all()
  orders = Order.objects.raw("""SELECT id, sum(orden_total), create_at 
                                FROM orders_order group by create_at""") 
  months = ['Enero', 'Febrero', 'Marzo', 'Abril', 'Mayo', 'Junio', 
            'Julio', 'Agosto', 'Septiembre', 'Octubre', 'Noviembre', 
            'Diciembre']
  
  for month in range(1,13):
        dataSource = dataSource
        orders = Order.objects.raw(f"""SELECT id, orden_total
                                    FROM orders_order where create_at
                                    between '{year}-{month}-01' and '{year}-{month}-31'""") 
        total_amount = 0
        for order in orders:
            total_amount += order.orden_total
        print(total_amount)
        dataSource["data"].append({"label": months[month - 1], "value": total_amount})

#   for category in categories:
#     dataSource["data"].append({"label": category.category_name, "value": '290'})
#   dataSource["data"].append({"label": 'Saudi', "value": '290'})
#   dataSource["data"].append({"label": 'Canada', "value": '180'})
#   dataSource["data"].append({"label": 'Iran', "value": '140'})
#   dataSource["data"].append({"label": 'Russia', "value": '115'})
#   dataSource["data"].append({"label": 'Russia', "value": '115'})
#   dataSource["data"].append({"label": 'UAE', "value": '100'})
#   dataSource["data"].append({"label": 'US', "value": '30'})
#   dataSource["data"].append({"label": 'China', "value": '30'})

# Create an object for the column 2D chart using the FusionCharts class constructor
# The chart data is passed to the `dataSource` parameter.
  column2D = FusionCharts("column2d", "myFirstChart", "1050", "400", "myFirstchart-container", "json", dataSource)
  return render(request, 'administrador/grafico.html', {
    'output': column2D.render()
}, )


dataSource = OrderedDict()
dataSource["data"] = []
 # The data for the chart should be in an array wherein each element of the array  is a JSON object having the `label` and `value` as keys.


def chart(request):

  dataSource = OrderedDict()  
  chartConfig = OrderedDict()
  chartConfig["caption"] = "Reportes de Ventas"
  chartConfig["subCaption"] = ""
  chartConfig["xAxisName"] = "Mes"
  chartConfig["yAxisName"] = "Total de ventas (Miles de pesos)"
  chartConfig["numberSuffix"] = "K"
  chartConfig["theme"] = "fusion"

  dataSource["chart"] = chartConfig
  dataSource["data"] = []
    # Create an object for the pie3d chart using the FusionCharts class constructor
  pie3d = FusionCharts("pie3d", "ex2" , "100%", "400", "chart-1", "json",
        # The data is passed as a string in the `dataSource` as parameter.
   {
        "chart": {
            "caption": "Poductos Mas vendidos",
            "subCaption" : "",
            "showValues":"1",
            "showPercentInTooltip" : "0",
            "numberPrefix" : "$",
            "enableMultiSlicing":"1",
            "theme": "fusion"
        },
        "data": [{
            "label": "Equity",
            "value": "300000"
        }, {
            "label": "Debt",
            "value": "230000"
        }, {
            "label": "Bullion",
            "value": "180000"
        }, {
            "label": "Real-estate",
            "value": "270000"
        }, {
            "label": "Insurance",
            "value": "20000"
        }]
    })

    # returning complete JavaScript and HTML code, which is used to generate chart in the browsers.
  return  render(request, 'administrador/grafico.html', {'output' : pie3d.render(), 'chartTitle': 'Pie 3D Chart'})










