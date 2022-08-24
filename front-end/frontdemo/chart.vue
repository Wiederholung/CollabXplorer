<template>
  <div id="main">
    <h1>查询结果</h1>
    <div id="chart1"style="height: 500px">

    </div>
  </div>
</template>

<script type="text/javascript">
import * as echarts from "echarts";
import $ from "jquery";
// 代码主体
export default {
  // 名字
  name: "chart",
  mounted() {
    // 获取页面div
    var myChart = echarts.init(document.getElementById('chart1'));
    var option;

    // 显示加载
    myChart.showLoading();

    // 获取json信息
    //https://raw.githubusercontent.com/Wiederholung/Academic-Collaboration-RS/main/back-end/file.json?token=GHSAT0AAAAAABXMP644TJRDVPMXYYO3IP62YYFWPRA
    $.getJSON('https://raw.githubusercontent.com/Wiederholung/Academic-Collaboration-RS/main/back-end/file.json?token=GHSAT0AAAAAABXMP644QZ7C2HNA3LEBFINSYYFYXNA', function (graph) {

      // 处理合作人数饼状图信息
      var piedata = [
        // {
        //   name:"国际学院",
        //   value:0
        // },
        // {
        //   name:"计算机学院",
        //   value:0
        // },
        // {
        //   name:"软件工程学院",
        //   value:0
        // },
        // {
        //   name:"数字媒体学院",
        //   value:0
        // },
        // {
        //   name:"马克思学院",
        //   value:0
        // },
        {
          name: "计算机学院",
          value:0
        },
        {name: "数字媒体与设计艺术学院",
          value:0
        },
        {
          name: "其他",
          value:0
        }
      ]
      for (var i = 0 ; i<graph.links.length ; i++){
        if (graph.links[i].source == "0"){
          piedata[graph.nodes[graph.links[i].target].category].value += graph.links[i].value
        }
        if (graph.links[i].target == "0"){
          piedata[graph.nodes[graph.links[i].source].category].value += graph.links[i].value
        }
      }

      // 处理合作文献数饼状图信息
      var piedata2 = [
        // {
        //   name:"国际学院",
        //   value:0
        // },
        // {
        //   name:"计算机学院",
        //   value:0
        // },
        // {
        //   name:"软件工程学院",
        //   value:0
        // },
        // {
        //   name:"数字媒体学院",
        //   value:0
        // },
        // {
        //   name:"马克思学院",
        //   value:0
        // },
        {
          name: "计算机学院",
          value:0
        },
        {name: "数字媒体与设计艺术学院",
          value:0
        },
        {
          name: "其他",
          value:0
        }
      ]
      for (var i = 0 ; i<graph.nodes.length ; i++){
        piedata2[graph.nodes[i].category].value += 1;
      }
      piedata2[graph.nodes[0].category].value --;

      // 关闭加载动画
      myChart.hideLoading();

      // 筛选展示的节点
      graph.nodes.forEach(function (node) {
        node.label = {
          show: node.symbolSize > 30
        };
      });

      // 中心关系图设置
      option = {
        // 标题设置
        title: {
          text: '跨领域合作关系表',
          subtext: 'Default layout',
          top: 'bottom',
          left: 'right'
        },
        // 提示框设计
        tooltip: {
          trigger:'item',
          formatter:function(parms){
            if (parms.data.type == "node"){
              return parms.data.name+"</br>文献数量:"+parms.data.value;
            }
            else if(parms.data.type == "link"){
              var startpoint = graph.nodes[parms.data.source].name;
              var endpoint = graph.nodes[parms.data.target].name;
              //"主笔人:"+startpoint+"</br>合作者:"+endpoint+"</br>此关系下合作数:"+parms.data.value
              return "合作者:"+endpoint+"</br>合作篇数:"+parms.data.value;
            }
            else {
              return ""
            }
          }
        },
        // 工具栏设置
        toolbox:{
          feature:{
            saveAsImage:{},
            dataView:{},
            restore:{}
          }
        },
        // 筛选栏设置
        legend: [
          {
            // selectedMode: 'single',
            data: graph.categories.map(function (a) {
              return a.name;
            })
          }
        ],
        // 动画设置
        animationDuration: 1500,
        animationEasingUpdate: 'quinticInOut',
        // 数据设置
        series: [
          // 关系图数据设置
          {
            name: '学者详细信息',
            type: 'graph',
            layout: 'none',
            data: graph.nodes,
            links: graph.links,
            categories: graph.categories,
            roam: false,
            label: {
              position: 'right',
              formatter: '{b}'
            },
            lineStyle: {
              color: 'source',
              curveness: 0,
            },
            emphasis: {
              //adjacency
              focus: 'adjacency',
              lineStyle: {
                width: 10
              }
            },
          },
          // 饼状图设置
          {
            type:'pie',
            name: '学者合作文献饼状图',
            data:piedata,
            label:{
              show:true,
              formatter:function (arg){
                return arg.name+":\n共合作"+arg.value+"篇"
              }
            },
            center:['88%',200],
            radius:45
          },
          {
            type:'pie',
            name: '学者合作人员饼状图',
            data:piedata2,
            label:{
              show:true,
              formatter:function (arg){
                return arg.name+":\n曾与"+arg.value+"人有过合作"
              }
            },
            center:['12%',200],
            radius:45
          }
        ]
      };
      myChart.setOption(option);
    });

    option && myChart.setOption(option);

    // 点击事件
    myChart.on('click',function (arg){
      console.log(arg)
      if (arg.data.name == '朱子炫'){
        myChart.showLoading();
        $.getJSON('../static/2.json', function (graph) {

          var piedata = [
            {
              name:"国际学院",
              value:0
            },
            {
              name:"计算机学院",
              value:0
            },
            {
              name:"软件工程学院",
              value:0
            },
            {
              name:"数字媒体学院",
              value:0
            },
            {
              name:"马克思学院",
              value:0
            },
          ]
          for (var i = 0 ; i<graph.links.length ; i++){
            if (graph.links[i].source == "2"){
              piedata[graph.nodes[graph.links[i].target].category].value += graph.links[i].value
            }
            if (graph.links[i].target == "2"){
              piedata[graph.nodes[graph.links[i].source].category].value += graph.links[i].value
            }
          }

          var piedata2 = [
            {
              name:"国际学院",
              value:0
            },
            {
              name:"计算机学院",
              value:0
            },
            {
              name:"软件工程学院",
              value:0
            },
            {
              name:"数字媒体学院",
              value:0
            },
            {
              name:"马克思学院",
              value:0
            },
          ]
          for (var i = 0 ; i<graph.nodes.length ; i++){
            piedata2[graph.nodes[i].category].value += 1;
          }
          piedata2[graph.nodes[0].category].value --;

          myChart.hideLoading();
          graph.nodes.forEach(function (node) {
            node.label = {
              show: node.symbolSize > 30
            };
          });
          option = {
            tooltip: {
              trigger:'item',
              formatter:function(parms){
                if (parms.data.type == "node"){
                  return parms.data.name+"</br>文献数量:"+parms.data.value;
                }
                else if(parms.data.type == "link"){
                  var startpoint = graph.nodes[parms.data.source].name;
                  var endpoint = graph.nodes[parms.data.target].name;
                  return "主笔人:"+startpoint+"</br>合作者:"+endpoint+"</br>此关系下合作数:"+parms.data.value;
                }
                else {
                  return ""
                }
              }
            },
            series: [
              {
                name: '学者详细信息',
                type: 'graph',
                layout: 'none',
                data: graph.nodes,
                links: graph.links,
                categories: graph.categories,
                roam: false,
                label: {
                  position: 'right',
                  formatter: '{b}'
                },
                lineStyle: {
                  color: 'source',
                  curveness: 0.3
                },
                emphasis: {
                  //adjacency
                  focus: 'adjacency',
                  lineStyle: {
                    width: 10
                  },

                }
              },
              {
                type:'pie',
                data:piedata,
                label:{
                  show:true,
                  formatter:function (arg){
                    return arg.name+":\n共合作"+arg.value+"篇"
                  }
                }
              },
              {
                type:'pie',
                data:piedata2,
                label:{
                  show:true,
                  formatter:function (arg){
                    return arg.name+":\n曾与"+arg.value+"人有过合作"
                  }
                }
              }
            ]
          };
          myChart.setOption(option);

        });
      }
      if (arg.data.name == '王俊翔'){
        myChart.showLoading();
        $.getJSON('../static/demodata.json', function (graph) {
          var piedata = [
            {
              name:"国际学院",
              value:0
            },
            {
              name:"计算机学院",
              value:0
            },
            {
              name:"软件工程学院",
              value:0
            },
            {
              name:"数字媒体学院",
              value:0
            },
            {
              name:"马克思学院",
              value:0
            },
          ]
          for (var i = 0 ; i<graph.links.length ; i++){
            if (graph.links[i].source == "0"){
              piedata[graph.nodes[graph.links[i].target].category].value += graph.links[i].value
            }
            if (graph.links[i].target == "0"){
              piedata[graph.nodes[graph.links[i].source].category].value += graph.links[i].value
            }
          }

          var piedata2 = [
            {
              name:"国际学院",
              value:0
            },
            {
              name:"计算机学院",
              value:0
            },
            {
              name:"软件工程学院",
              value:0
            },
            {
              name:"数字媒体学院",
              value:0
            },
            {
              name:"马克思学院",
              value:0
            },
          ]
          for (var i = 0 ; i<graph.nodes.length ; i++){
            piedata2[graph.nodes[i].category].value += 1;
          }
          piedata2[graph.nodes[0].category].value --;

          myChart.hideLoading();
          graph.nodes.forEach(function (node) {
            node.label = {
              show: node.symbolSize > 30
            };
          });
          option = {
            tooltip: {
              trigger:'item',
              formatter:function(parms){
                if (parms.data.type == "node"){
                  return parms.data.name+"</br>文献数量:"+parms.data.value;
                }
                else if(parms.data.type == "link"){
                  var startpoint = graph.nodes[parms.data.source].name;
                  var endpoint = graph.nodes[parms.data.target].name;
                  return "主笔人:"+startpoint+"</br>合作者:"+endpoint+"</br>此关系下合作数:"+parms.data.value;
                }
                else {
                  return ""
                }
              }
            },
            series: [
              {
                name: '学者详细信息',
                type: 'graph',
                layout: 'none',
                data: graph.nodes,
                links: graph.links,
                categories: graph.categories,
                roam: false,
                label: {
                  position: 'right',
                  formatter: '{b}'
                },
                lineStyle: {
                  color: 'source',
                  curveness: 0.3
                },
                emphasis: {
                  //adjacency
                  focus: 'adjacency',
                  lineStyle: {
                    width: 10
                  },

                }
              },
              {
                type:'pie',
                data:piedata,
                label:{
                  show:true,
                  formatter:function (arg){
                    return arg.name+":\n共合作"+arg.value+"篇"
                  }
                }
              },
              {
                type:'pie',
                data:piedata2,
                label:{
                  show:true,
                  formatter:function (arg){
                    return arg.name+":\n曾与"+arg.value+"人有过合作"
                  }
                }
              }
            ]
          };
          myChart.setOption(option);

        });
      }

    })
  }
}
</script>

<style scoped>
#main{
  text-align: center
}
#chart1{
  text-align: center
}
</style>



<!--<template>-->
<!--  <div id="main">-->
<!--    <h1>查询结果</h1>-->
<!--    <div id="chart1"style="height: 600px">-->

<!--    </div>-->
<!--    <div id="chart2"style="height: 600px">-->

<!--    </div>-->
<!--  </div>-->
<!--</template>-->

<!--<script type="text/javascript">-->
<!--import * as echarts from "echarts";-->
<!--import $ from "jquery";-->
<!--export default {-->
<!--  name: "chart",-->
<!--  mounted() {-->
<!--    var myChart = echarts.init(document.getElementById('chart1'));-->
<!--    var option;-->

<!--    myChart.showLoading();-->
<!--    $.getJSON('../static/demodata.json', function (graph) {-->
<!--      myChart.hideLoading();-->
<!--      graph.nodes.forEach(function (node) {-->
<!--        node.label = {-->
<!--          show: node.symbolSize > 30-->
<!--        };-->
<!--      });-->
<!--      option = {-->
<!--        title: {-->
<!--          text: '跨领域合作关系表',-->
<!--          subtext: 'Default layout',-->
<!--          top: 'bottom',-->
<!--          left: 'right'-->
<!--        },-->
<!--        tooltip: {-->
<!--          trigger:'item',-->
<!--          formatter:function(parms){-->
<!--            if (parms.data.type == "node"){-->
<!--              return parms.data.name+"</br>文献数量:"+parms.data.value;-->
<!--            }-->
<!--            else if(parms.data.type == "link"){-->
<!--              var startpoint = graph.nodes[parms.data.source].name;-->
<!--              var endpoint = graph.nodes[parms.data.target].name;-->
<!--              return "主笔人:"+startpoint+"</br>合作者:"+endpoint+"</br>此关系下合作数:"+parms.data.value;-->
<!--            }-->
<!--            else {-->
<!--              return ""-->
<!--            }-->
<!--          }-->
<!--        },-->
<!--        toolbox:{-->
<!--          feature:{-->
<!--            saveAsImage:{},-->
<!--            dataView:{},-->
<!--            restore:{}-->
<!--          }-->
<!--        },-->
<!--        legend: [-->
<!--          {-->
<!--            // selectedMode: 'single',-->
<!--            data: graph.categories.map(function (a) {-->
<!--              return a.name;-->
<!--            })-->
<!--          }-->
<!--        ],-->
<!--        animationDuration: 1500,-->
<!--        animationEasingUpdate: 'quinticInOut',-->
<!--        series: [-->
<!--          {-->
<!--            name: '学者详细信息',-->
<!--            type: 'graph',-->
<!--            layout: 'none',-->
<!--            data: graph.nodes,-->
<!--            links: graph.links,-->
<!--            categories: graph.categories,-->
<!--            roam: false,-->
<!--            label: {-->
<!--              position: 'right',-->
<!--              formatter: '{b}'-->
<!--            },-->
<!--            lineStyle: {-->
<!--              color: 'source',-->
<!--              curveness: 0.3-->
<!--            },-->
<!--            emphasis: {-->
<!--              //adjacency-->
<!--              focus: 'adjacency',-->
<!--              lineStyle: {-->
<!--                width: 10-->
<!--              },-->

<!--            }-->
<!--          }-->
<!--        ]-->
<!--      };-->
<!--      myChart.setOption(option);-->
<!--    });-->

<!--    option && myChart.setOption(option);-->

<!--    var myChart2 = echarts.init(document.getElementById('chart2'));-->
<!--    var option2;-->

<!--    myChart.showLoading();-->
<!--    $.getJSON('../static/demodata.json', function (graph) {-->
<!--      var piedata = [-->
<!--        {-->
<!--          name:"国际学院",-->
<!--          value:0-->
<!--        },-->
<!--        {-->
<!--          name:"计算机学院",-->
<!--          value:0-->
<!--        },-->
<!--        {-->
<!--          name:"软件工程学院",-->
<!--          value:0-->
<!--        },-->
<!--        {-->
<!--          name:"数字媒体学院",-->
<!--          value:0-->
<!--        },-->
<!--        {-->
<!--          name:"马克思学院",-->
<!--          value:0-->
<!--        },-->
<!--      ]-->
<!--      for (var i = 0 ; i<graph.links.length ; i++){-->
<!--        if (graph.links[i].source == "0"){-->
<!--          piedata[graph.nodes[graph.links[i].target].category].value += graph.links[i].value-->
<!--        }-->
<!--        if (graph.links[i].target == "0"){-->
<!--          piedata[graph.nodes[graph.links[i].source].category].value += graph.links[i].value-->
<!--        }-->
<!--      }-->
<!--      option2 = {-->
<!--        series:[-->
<!--          {-->
<!--            type:'pie',-->
<!--            data:piedata,-->
<!--            label:{-->
<!--              show:true,-->
<!--              formatter:function (arg){-->
<!--                return arg.name+"\n共合作"+arg.value+"篇"-->
<!--              }-->
<!--            }-->
<!--          }-->
<!--        ]-->
<!--      }-->

<!--      myChart2.setOption(option2);-->
<!--    });-->

<!--    option2 && myChart2.setOption(option2);-->

<!--    myChart.on('click',function (arg){-->
<!--      console.log(arg)-->
<!--      if (arg.data.name == '朱子炫'){-->
<!--        myChart.showLoading();-->
<!--        $.getJSON('../static/demodata2.json', function (graph) {-->
<!--          myChart.hideLoading();-->
<!--          graph.nodes.forEach(function (node) {-->
<!--            node.label = {-->
<!--              show: node.symbolSize > 30-->
<!--            };-->
<!--          });-->
<!--          option = {-->
<!--            tooltip: {-->
<!--              trigger:'item',-->
<!--              formatter:function(parms){-->
<!--                if (parms.data.type == "node"){-->
<!--                  return parms.data.name+"</br>文献数量:"+parms.data.value;-->
<!--                }-->
<!--                else if(parms.data.type == "link"){-->
<!--                  var startpoint = graph.nodes[parms.data.source].name;-->
<!--                  var endpoint = graph.nodes[parms.data.target].name;-->
<!--                  return "主笔人:"+startpoint+"</br>合作者:"+endpoint+"</br>此关系下合作数:"+parms.data.value;-->
<!--                }-->
<!--                else {-->
<!--                  return ""-->
<!--                }-->
<!--              }-->
<!--            },-->
<!--            series: [-->
<!--              {-->
<!--                name: '学者详细信息',-->
<!--                type: 'graph',-->
<!--                layout: 'none',-->
<!--                data: graph.nodes,-->
<!--                links: graph.links,-->
<!--                categories: graph.categories,-->
<!--                roam: false,-->
<!--                label: {-->
<!--                  position: 'right',-->
<!--                  formatter: '{b}'-->
<!--                },-->
<!--                lineStyle: {-->
<!--                  color: 'source',-->
<!--                  curveness: 0.3-->
<!--                },-->
<!--                emphasis: {-->
<!--                  //adjacency-->
<!--                  focus: 'adjacency',-->
<!--                  lineStyle: {-->
<!--                    width: 10-->
<!--                  },-->

<!--                }-->
<!--              }-->
<!--            ]-->
<!--          };-->
<!--          myChart.setOption(option);-->

<!--          var piedata = [-->
<!--            {-->
<!--              name:"国际学院",-->
<!--              value:0-->
<!--            },-->
<!--            {-->
<!--              name:"计算机学院",-->
<!--              value:0-->
<!--            },-->
<!--            {-->
<!--              name:"软件工程学院",-->
<!--              value:0-->
<!--            },-->
<!--            {-->
<!--              name:"数字媒体学院",-->
<!--              value:0-->
<!--            },-->
<!--            {-->
<!--              name:"马克思学院",-->
<!--              value:0-->
<!--            },-->
<!--          ]-->
<!--          for (var i = 0 ; i<graph.links.length ; i++){-->
<!--            if (graph.links[i].source == "0"){-->
<!--              piedata[graph.nodes[graph.links[i].target].category].value += graph.links[i].value-->
<!--            }-->
<!--            if (graph.links[i].target == "0"){-->
<!--              piedata[graph.nodes[graph.links[i].source].category].value += graph.links[i].value-->
<!--            }-->
<!--          }-->
<!--          option2 = {-->
<!--            series:[-->
<!--              {-->
<!--                type:'pie',-->
<!--                data:piedata,-->
<!--                label:{-->
<!--                  show:true,-->
<!--                  formatter:function (arg){-->
<!--                    return arg.name+"\n共合作"+arg.value+"篇"-->
<!--                  }-->
<!--                }-->
<!--              }-->
<!--            ]-->
<!--          }-->

<!--          myChart2.setOption(option2);-->
<!--        });-->
<!--      }-->
<!--      if (arg.data.name == '王俊翔'){-->
<!--        myChart.showLoading();-->
<!--        $.getJSON('../static/demodata.json', function (graph) {-->
<!--          myChart.hideLoading();-->
<!--          graph.nodes.forEach(function (node) {-->
<!--            node.label = {-->
<!--              show: node.symbolSize > 30-->
<!--            };-->
<!--          });-->
<!--          option = {-->
<!--            tooltip: {-->
<!--              trigger:'item',-->
<!--              formatter:function(parms){-->
<!--                if (parms.data.type == "node"){-->
<!--                  return parms.data.name+"</br>文献数量:"+parms.data.value;-->
<!--                }-->
<!--                else if(parms.data.type == "link"){-->
<!--                  var startpoint = graph.nodes[parms.data.source].name;-->
<!--                  var endpoint = graph.nodes[parms.data.target].name;-->
<!--                  return "主笔人:"+startpoint+"</br>合作者:"+endpoint+"</br>此关系下合作数:"+parms.data.value;-->
<!--                }-->
<!--                else {-->
<!--                  return ""-->
<!--                }-->
<!--              }-->
<!--            },-->
<!--            series: [-->
<!--              {-->
<!--                name: '学者详细信息',-->
<!--                type: 'graph',-->
<!--                layout: 'none',-->
<!--                data: graph.nodes,-->
<!--                links: graph.links,-->
<!--                categories: graph.categories,-->
<!--                roam: false,-->
<!--                label: {-->
<!--                  position: 'right',-->
<!--                  formatter: '{b}'-->
<!--                },-->
<!--                lineStyle: {-->
<!--                  color: 'source',-->
<!--                  curveness: 0.3-->
<!--                },-->
<!--                emphasis: {-->
<!--                  //adjacency-->
<!--                  focus: 'adjacency',-->
<!--                  lineStyle: {-->
<!--                    width: 10-->
<!--                  },-->

<!--                }-->
<!--              }-->
<!--            ]-->
<!--          };-->
<!--          myChart.setOption(option);-->

<!--          var piedata = [-->
<!--            {-->
<!--              name:"国际学院",-->
<!--              value:0-->
<!--            },-->
<!--            {-->
<!--              name:"计算机学院",-->
<!--              value:0-->
<!--            },-->
<!--            {-->
<!--              name:"软件工程学院",-->
<!--              value:0-->
<!--            },-->
<!--            {-->
<!--              name:"数字媒体学院",-->
<!--              value:0-->
<!--            },-->
<!--            {-->
<!--              name:"马克思学院",-->
<!--              value:0-->
<!--            },-->
<!--          ]-->
<!--          for (var i = 0 ; i<graph.links.length ; i++){-->
<!--            if (graph.links[i].source == "0"){-->
<!--              piedata[graph.nodes[graph.links[i].target].category].value += graph.links[i].value-->
<!--            }-->
<!--            if (graph.links[i].target == "0"){-->
<!--              piedata[graph.nodes[graph.links[i].source].category].value += graph.links[i].value-->
<!--            }-->
<!--          }-->
<!--          option2 = {-->
<!--            series:[-->
<!--              {-->
<!--                type:'pie',-->
<!--                data:piedata,-->
<!--                label:{-->
<!--                  show:true,-->
<!--                  formatter:function (arg){-->
<!--                    return arg.name+"\n共合作"+arg.value+"篇"-->
<!--                  }-->
<!--                }-->
<!--              }-->
<!--            ]-->
<!--          }-->

<!--          myChart2.setOption(option2);-->
<!--        });-->
<!--      }-->

<!--    })-->
<!--  }-->
<!--}-->
<!--</script>-->

<!--<style scoped>-->
<!--#main{-->
<!--  text-align: center-->
<!--}-->
<!--#chart1{-->
<!--  text-align: center-->
<!--}-->
<!--#chart2{-->
<!--  text-align: center-->
<!--}-->
<!--</style>-->
