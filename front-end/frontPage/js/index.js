$(function () {



	leidatu();
	wuran();
	huaxing();
	yanjiutu();
	map();
	// zhexian();

	//大屏

	function leida1() {
		var myChart = echarts.init(document.getElementById('map'));


		myChart.setOption(option);
		window.addEventListener("resize", function () {
			myChart.resize();
		});

	}




})


function map() {
		// var myChart = echarts.init(document.getElementById('map'));
		// myChart.showLoading();
		// $.getJSON('./fenglei.json', function (graph) {
		//
		// 		// 关闭加载动画
		// 		myChart.hideLoading();
		//
		// 		graph.nodes.forEach(function (node) {
		// 	node.label = {
		// 		show: node.symbolSize > 25
		// 	};
		// });
		//
		// 		// 中心关系图设置
		// 		option = {
		// 			// 标题设置
		// 			title: {
		// 				text: '跨领域合作关系表',
		// 				subtext: 'Default layout',
		// 				top: 'bottom',
		// 				left: 'right'
		// 			},
		// 			textStyle: {
		// 				//字体风格,'normal','italic','oblique'
		// 				fontStyle: 'oblique',
		// 				textbordercolor: '#FFF',
		// 				fontSize: 12,
		// 				color: '#FFF',
		// 				fontWeight: 'bold',
		// 				textshadowColor: '#FFFFFF',
		// 			},
		// 			// 提示框设计
		// 			tooltip: {
		// 				trigger: 'item',
		// 				formatter: function (parms) {
		// 					if (parms.data.type == "node") {
		// 						return parms.data.name + "</br>文献数量:" + parms.data.value;
		// 					} else if (parms.data.type == "link") {
		// 						for (var i = 0; i < graph.nodes.length; i++) {
		// 							if (parms.data.target === graph.nodes[i].id) {
		// 								var endpoint = graph.nodes[i].name;
		// 								break
		// 							}
		// 						}
		// 						//"主笔人:"+startpoint+"</br>合作者:"+endpoint+"</br>此关系下合作数:"+parms.data.value
		// 						return "合作者:" + endpoint + "</br>合作篇数:" + parms.data.value;
		// 					} else {
		// 						return ""
		// 					}
		// 				}
		// 			},
		// 			// 工具栏设置
		// 			toolbox: {
		// 				feature: {
		// 					saveAsImage: {},
		// 					dataView: {},
		// 					restore: {}
		// 				}
		// 			},
		// 			// 筛选栏设置
		// 			legend: [
		// 				{
		// 					// selectedMode: 'single',
		// 					data: graph.categories.map(function (a) {
		// 						return a.name;
		// 					})
		// 				}
		// 			],
		// 			color: ["#845EC2", "#66CCFF", "#FF6F91", "#FF9671", "#FFC75F", "#C4FCEF", "#F3C5FF", "#00C9A7", "#F9F871"],
		// 			// 动画设置
		// 			animationDuration: 1500,
		// 			animationEasingUpdate: 'quinticInOut',
		// 			// 数据设置
		// 			series: [
		// 				// 关系图数据设置
		// 				{
		// 					name: '学者详细信息',
		// 					type: 'graph',
		// 					layout: 'none',
		// 					data: graph.nodes,
		// 					links: graph.links,
		// 					categories: graph.categories,
		// 					roam: false,
		// 					label: {
		// 						position: 'right',
		// 						formatter: '{b}'
		// 					},
		// 					lineStyle: {
		// 						color: 'source',
		// 						curveness: 0,
		// 					},
		// 					emphasis: {
		// 						//adjacency
		// 						focus: 'adjacency',
		// 						lineStyle: {
		// 							width: 10
		// 						}
		// 					},
		// 				},
		// 			]
		// 		};
		// 		myChart.setOption(option);
		// 	}
		// );
		// myChart.on('click', function (params) {
		// 	console.log(params);
		// });
		// option && myChart.setOption(option);
		//
		// window.addEventListener("resize", function () {
		// 	myChart.resize();
		// });
	var myChart = echarts.init(document.getElementById('map'));
	myChart.showLoading();
	i = 9
	$.getJSON('./result'+i+'.json', function (graph) {
		myChart.hideLoading();
		graph.nodes.forEach(function (node) {
			node.label = {
				show: node.symbolSize > 25
			};
		});
		option = {
			title: {
				text: '跨学科合作推荐',
				subtext: 'Default layout',
				top: 'bottom',
				left: 'right'
			},
			tooltip: {},
			legend: [
				{
					// selectedMode: 'single',
					data: graph.categories.map(function (a) {
						return a.name;
					}),
					textStyle: {
						color: '#fff'
					},
				}
			],
			//设置字体
			textStyle: {
				//字体风格,'normal','italic','oblique'
				fontStyle: 'oblique',
				textbordercolor: '#FFF',
				fontSize: 12,
				color: '#FFF',
				fontWeight: 'bold',
				textshadowColor: '#FFFFFF',
			},
			animationDuration: 1500,
			animationEasingUpdate: 'quinticInOut',
			series: [
				{
					name: '跨学科合作推荐',
					type: 'graph',
					layout: 'none',
					data: graph.nodes,
					links: graph.links,
					categories: graph.categories,
					roam: true,
					label: {
						position: 'right',
						formatter: '{b}'
					},
					lineStyle: {
						color: 'source',
						curveness: 0.3
					},
					emphasis: {
						focus: 'adjacency',
						lineStyle: {
							width: 10
						}
					},

				}
			]
		};
		myChart.setOption(option);
	});
	// myChart.on('click', function (params) {
	// 	console.log(params);
	// });
	myChart.setOption(option);
	window.addEventListener("resize", function () {
		myChart.resize();
	});

}


function leidatu() {
	// var imgPath = ['http://bmob-cdn-15355.b0.upaiyun.com/2017/12/01/bee4341c4089af7980b87074a77479ad.png']
	var myChart = echarts.init(document.getElementById('leida'));

	const data = [["2000", 2], ["2001", 5], ["2002", 7], ["2003", 6], ["2004", 5], ["2005", 9], ["2006", 10], ["2007", 16], ["2008", 11], ["2009", 10], ["2010", 14], ["2011", 13], ["2012", 12], ["2013", 10], ["2014", 7], ["2015", 6], ["2016", 4], ["2017", 3], ["2018", 1], ["2019", 1], ["2020", 2], ["2021", 1], ["2022", 0]];
	const dateList = data.map(function (item) {
		return item[0];
	});
	const valueList = data.map(function (item) {
		return item[1];
	});
	option = {
		// Make gradient line here
		visualMap: [
			{
				show: false,
				type: 'continuous',
				seriesIndex: 0,
				min: 0,
				max: 500
			},
			{
				show: false,
				type: 'continuous',
				seriesIndex: 1,
				dimension: 0,
				min: 0,
				max: dateList.length - 1
			}
		],
		title: [
			{
				left: 'center',
				text: ''
			}
		],
		tooltip: {
			trigger: 'axis'
		},
		xAxis: [
			{
				data: dateList
			},
			{
				data: dateList,
				gridIndex: 1
			}
		],
		yAxis: [
			{},
			{
				gridIndex: 1
			}
		],
		grid: [
			{
				bottom: '60%'
			},
			{
				top: '60%'
			}
		],
		series: [
			{
				type: 'line',
				showSymbol: false,
				data: valueList
			},
			{
				type: 'line',
				showSymbol: false,
				data: valueList,
				xAxisIndex: 1,
				yAxisIndex: 1
			}
		]
	};


	myChart.setOption(option);
}

function wuran() {

	var myChart = echarts.init(document.getElementById('wuran'));
	var salvProName = ["企业总数", "废气企业", "废水企业", "铅污染", "铬污染"];
	var salvProValue = [117, 74, 72, 67, 55];
	var salvProMax = [];//背景按最大值
	for (let i = 0; i < salvProValue.length; i++) {
		salvProMax.push(salvProValue[0])
	}
	option = {
		xAxis: {
			type: 'category',
			boundaryGap: false,
			data: ['2000', '2001', '2002', '2003', '2004', '2005', '2006', '2007', '2008', '2009', '2010', , '2011', '2012', '2013', '2014', '2015', '2016', '2017', '2018', '2019', '2020', '2021', '2022']
		},
		yAxis: {
			type: 'value'
		},
		series: [
			{
				data: [2, 7, 14, 20, 25, 34, 44, 60, 71, 81, 95, 108, 120, 130, 137, 143, 147, 150, 151, 152, 154, 155, 155],
				type: 'line',
				areaStyle: {}
			}
		]
	};

	myChart.setOption(option);


}

function huaxing() {
	var myChart = echarts.init(document.getElementById('huaxing'));

	var dataStyle = {
		normal: {
			label: {
				show: false
			},
			labelLine: {
				show: false
			},
			shadowBlur: 0,
			shadowColor: '#203665'
		}
	};
	option = {

		series: [{
			name: '第一个圆环',
			type: 'pie',
			clockWise: false,
			radius: [45, 55],
			itemStyle: dataStyle,
			hoverAnimation: false,
			center: ['15%', '50%'],
			data: [{
				value: 15,
				label: {
					normal: {
						rich: {
							a: {
								color: '#3a7ad5',
								align: 'center',
								fontSize: 14,
								fontWeight: "bold"
							},
							b: {
								color: '#fff',
								align: 'center',
								fontSize: 12
							}
						},
						formatter: function (params) {
							return "{b|医疗}\n\n" + "{a|" + params.value + "%}";
						},
						position: 'center',
						show: true,
						textStyle: {
							fontSize: '12',
							fontWeight: 'normal',
							color: '#fff'
						}
					}
				},
				itemStyle: {
					normal: {
						color: '#2c6cc4',
						shadowColor: '#2c6cc4',
						shadowBlur: 0
					}
				}
			}, {
				value: 75,
				name: 'invisible',
				itemStyle: {
					normal: {
						color: '#24375c'
					},
					emphasis: {
						color: '#24375c'
					}
				}
			}]
		}, {
			name: '第二个圆环',
			type: 'pie',
			clockWise: false,
			radius: [45, 55],
			itemStyle: dataStyle,
			hoverAnimation: false,
			center: ['50%', '50%'],
			data: [{
				value: 35,
				label: {
					normal: {
						rich: {
							a: {
								color: '#d03e93',
								align: 'center',
								fontSize: 14,
								fontWeight: "bold"
							},
							b: {
								color: '#fff',
								align: 'center',
								fontSize: 12
							}
						},
						formatter: function (params) {
							return "{b|通信}\n\n" + "{a|" + params.value + "%}";
						},
						position: 'center',
						show: true,
						textStyle: {
							fontSize: '12',
							fontWeight: 'normal',
							color: '#fff'
						}
					}
				},
				itemStyle: {
					normal: {
						color: '#ef45ac',
						shadowColor: '#ef45ac',
						shadowBlur: 0
					}
				}
			}, {
				value: 50,
				name: 'invisible',
				itemStyle: {
					normal: {
						color: '#412a4e'
					},
					emphasis: {
						color: '#412a4e'
					}
				}
			}]
		}, {
			name: '第三个圆环',
			type: 'pie',
			clockWise: false,
			radius: [45, 55],
			itemStyle: dataStyle,
			hoverAnimation: false,
			center: ['85%', '50%'],
			data: [{
				value: 50,
				label: {
					normal: {
						rich: {
							a: {
								color: '#FF9912',
								align: 'center',
								fontSize: 14,
								fontWeight: "bold"
							},
							b: {
								color: '#fff',
								align: 'center',
								fontSize: 12
							}
						},
						formatter: function (params) {
							return "{b|计算机}\n\n" + "{a|" + params.value + "%}";
						},
						position: 'center',
						show: true,
						textStyle: {
							fontSize: '12',
							fontWeight: 'normal',
							color: '#fff'
						}
					}
				},
				itemStyle: {
					normal: {
						color: '#FF9912',
						shadowColor: '#FF9912',
						shadowBlur: 0
					}
				}
			}, {
				value: 25,
				name: 'invisible',
				itemStyle: {
					normal: {
						color: '#695B00'
					},
					emphasis: {
						color: '#695B00'
					}
				}
			}]
		}]
	}

	myChart.setOption(option);


}


// function zhexian() {
// 	var myChart = echarts.init(document.getElementById('zhexian'));

// 	dataText = [{
// 		name: '上游流速',
// 		type: 'line',
// 		smooth: true,
// 		symbolSize: 8,
// 		data: [127, 224, 120, 278, 227, 237],
// 		barWidth: '30%',
// 		itemStyle: {
// 			normal: {
// 				color: '#f0c725'
// 			}
// 		}
// 	}, {
// 		name: '下游流速',
// 		type: 'line',
// 		smooth: true,
// 		symbolSize: 8,
// 		data: [27, 124, 70, 178, 127, 157],
// 		barWidth: '30%',
// 		itemStyle: {
// 			normal: {
// 				color: '#16f892'
// 			}
// 		}
// 	},
// 	{
// 		name: '平均流速',
// 		type: 'line',
// 		smooth: true,
// 		symbolSize: 8,
// 		data: [127, 74, 120, 99, 130, 355],
// 		barWidth: '30%',
// 		itemStyle: {
// 			normal: {
// 				color: '#0BE3FF'
// 			}
// 		}
// 	}
// 	]
// 	dataObj = {
// 		year: ['2015', '2016', '2017', '2018', '2019', '2020'],
// 		data: {
// 			value: [{
// 				name: '上游流速',
// 				value: [127, 224, 250, 278, 227, 355]
// 			}, {
// 				name: '下游流速',
// 				value: [27, 124, 70, 178, 127, 157]
// 			}, {
// 				name: '平均流速',
// 				value: [127, 74, 120, 99, 130, 50]
// 			}]
// 		}
// 	}
// 	let dataArr = []

// 	dataObj.data.value.map(item => {
// 		let datachild = []
// 		let newArr = {
// 			name: item.name,
// 			type: 'line',
// 			smooth: true,
// 			symbolSize: 8,
// 			data: item.value,
// 			barWidth: '30%',
// 			itemStyle: {
// 				normal: {
// 					color: item.name === '上游流速' ? '#f0c725' : item.name === '下游流速' ? '#0BE3FF' : '#16f892'
// 				}
// 			}
// 		}

// 		dataArr.push(newArr)
// 	})
// 	option = {
// 		color: ['#f0c725', '#16f892'],
// 		title: {
// 			left: 'center',
// 			text: '',
// 			textStyle: {
// 				color: '#FFFFFF',
// 				fontSize: '14',
// 			}
// 		},
// 		tooltip: {
// 			trigger: 'axis',
// 			axisPointer: { // 坐标轴指示器，坐标轴触发有效
// 				type: 'shadow' // 默认为直线，可选为：'line' | 'shadow'
// 			}
// 		},
// 		legend: {
// 			x: 'center',
// 			top: '25',
// 			textStyle: {
// 				color: '#c1cadf',
// 				"fontSize": 14
// 			}
// 		},
// 		grid: {
// 			left: '6%',
// 			right: '4%',
// 			top: '25%',
// 			bottom: '3%',
// 			containLabel: true
// 		},
// 		toolbox: {
// 			show: true,
// 			orient: 'vertical',
// 			x: 'right',
// 			y: 'center'
// 		},
// 		xAxis: [{
// 			type: 'category',
// 			boundaryGap: false,
// 			data: dataObj.year,
// 			axisLine: {
// 				lineStyle: {
// 					color: 'rgba(240,199,37,0.5)'
// 				}
// 			},
// 			axisLabel: {
// 				interval: 0,
// 				color: '#c1cadf',
// 				fontSize: '15'
// 			}
// 		}],
// 		yAxis: [{
// 			type: 'value',
// 			name: '(m3)',
// 			nameTextStyle: {
// 				color: '#c1cadf',
// 				align: 'right',
// 				lineHeight: 10
// 			},
// 			axisLine: {
// 				lineStyle: {
// 					color: 'rgba(240,199,37,0.5)'
// 				}
// 			},
// 			axisLabel: {
// 				interval: 0,
// 				color: '#c1cadf',
// 				fontSize: '15'
// 			},
// 			splitLine: {
// 				show: false
// 			}
// 		}],
// 		series: dataArr
// 	};
// 	//大屏
// 	/*var myChart = echarts.init(document.getElementById('channel_handle_detail'));
// 	myChart.clear();
// 	if(data.handleTimeData.length>0){
// 		myChart.setOption(option);
// 	}else{
// 		noDataTip($("#channel_handle_detail"));
// 	}*/
// 	// 使用刚指定的配置项和数据显示图表。
// 	myChart.setOption(option);
// 	window.addEventListener("resize", function () {
// 		myChart.resize();
// 	});
// }
function yanjiutu() {
	var myChart = echarts.init(document.getElementById('yanjiu'));


	var data = [
		{
			name: '医疗',
			value: 15,
			children: [
				{
					name: '脑机接口',
					value: 7,
					children: [
						{
							name: 'Scholars33',
							value: 3
						},
						{
							name: 'Scholars65',
							value: 4,
						}
					]
				},
				{
					name: '生物芯片',
					value: 8,
					children: [
						// {
						//   name: 'Scholars22',
						//   value: 3
						// },
						{
							name: 'Scholars44',
							value: 5
						}
					]
				}
			]
		},
		{
			name: '通讯',
			value: 35,
			children: [
				{
					name: '多媒体',
					value: 15,
					children: [
						// {
						//   name: 'Scholars6',
						//   value: 11
						// },
						{
							name: 'Scholars16',
							value: 4
						}
					]
				},
				{
					name: '无线通讯',
					value: 20,
					children: [
						{
							name: 'Scholars32',
							value: 10
						},
						{
							name: 'Scholars26',
							value: 10
						}
					]
				}
			]
		},
		{
			name: '计算机',
			value: 50,
			children: [
				{
					name: '软件工程',
					value: 20,
					children: [
						{
							name: 'Scholars57',
							value: 17
						},
						{
							name: 'Scholars61',
							value: 3
						}
					]
				},
				{
					name: '人工智能',
					value: 15,
					children: [
						//   {
						// 	name: 'Scholars47',
						// 	value: 7
						//   },
						{
							name: 'Scholars20',
							value: 8
						}
					]
				},
				{
					name: '计算机视觉',
					value: 15,
					children: [
						{
							name: 'Scholars41',
							value: 10
						},
						//   {
						// 	name: 'Scholars38',
						// 	value: 5
						//   }
					]
				}
			]
		}
	];
	option = {
		color: ["#845EC2", "#66CCFF", "#FF6F91", "#FF9671", "#FFC75F", "#C4FCEF", "#F3C5FF", "#00C9A7", "#F9F871"],
		series: {
			type: 'sunburst',
			// emphasis: {
			//     focus: 'ancestor'
			// },
			data: data,
			emphasis: {
				focus: 'ancestor'
			},
			radius: [0, '100%'],
			itemStyle: {
				borderRadius: 4,
				borderWidth: 2
			},
			label: {
				rotate: 'radial',
				minAngle: 15,
				textStyle: {
					color: '#606060',
					fontSize: 12
				},
			}
		}
	};

	// option = {
	// 	tooltip: {
	// 		trigger: 'item'
	// 	},
	// 	legend: {
	// 		top: '5%',
	// 		left: 'center',
	// 		textStyle: {
	// 			color: 'rgba(255, 255, 255, 0.9)'
	// 		}
	// 	},
	// 	series: [
	// 		{
	// 			name: 'Access From',
	// 			type: 'pie',
	// 			radius: ['40%', '70%'],
	// 			avoidLabelOverlap: false,
	// 			// itemStyle: {
	// 			//   borderRadius: 10,
	// 			//   borderColor: '#fff',
	// 			//   borderWidth: 2
	// 			// },
	// 			label: {
	// 				show: false,
	// 				position: 'center'
	// 			},
	// 			// emphasis: {
	// 			//   label: {
	// 			// 	show: true,
	// 			// 	fontSize: 15,
	// 			// 	fontWeight: 'bold'
	// 			//   }
	// 			// },
	// 			labelLine: {
	// 				show: false
	// 			},
	// 			data: [
	// 				{ value: 26, name: '软件工程' },
	// 				{ value: 15, name: '人工智能' },
	// 				{ value: 9, name: '脑机接口' },
	// 				{ value: 6, name: '神经网络' },
	// 				{ value: 20, name: '无线通讯' },
	// 				{ value: 14, name: '多媒体' }
	// 			]
	// 		}
	// 	]
	// };

	myChart.setOption(option);
	window.addEventListener("resize", function () {
		myChart.resize();
	});
}