let trace1 = {
    type: 'bar',
    name:'Family',
    x: [ 'Australia', 'Germany', 'United_States','India','France','United_Kingdom',"Canada",'Pakistan'],
    y: [
        Australia[0].count, 
        Germany[0].count,
        United_States[0].count,
        India[0].count,
        France[0].count,
        United_kingdom[0].count,
        Canada[0].count,
        Pakistan[0].count
    ],
    textfont:{
        size:13,
        color:'white'
    },
    width: 0.18,
    marker:{
        color:'blue'
    }
};

// trace1.text = trace1.y;
let trace2 = {
    type: 'bar',
    name:'Premium',
    x: ['Australia', 'Germany', 'United_States','India','France','United_Kingdom',"Canada",'Pakistan'],
    y: [
        Australia[1].count, 
        Germany[1].count,
        United_States[1].count,
        India[1].count,
        France[1].count,
        United_kingdom[1].count,
        Canada[1].count,
        Pakistan[1].count
    ],
    
    textfont:{
        size:13,
        color:'white'
    },
    width: 0.18,
    marker:{
        color:'orange'
    }
};

// trace2.text = trace2.y;

let trace3 = {
    type: 'bar',
    name:'Student',
    x: ['Australia', 'Germany', 'United_States','India','France','United_Kingdom',"Canada",'Pakistan'],
    y: [
        Australia[2].count, 
        Germany[2].count,
        United_States[2].count,
        India[2].count,
        France[2].count,
        United_kingdom[2].count,
        Canada[2].count,
        Pakistan[2].count
    ],
    textfont:{
        size:13,
        color:'white'
    },
    width: 0.18,
    marker:{
        color:'green'
    }
};

// trace3.text = trace3.y;

let trace4 = {
    type: 'bar',
    name:'Free',    
    x: ['Australia', 'Germany', 'United_States','India','France','United_Kingdom',"Canada",'Pakistan'],
    y: [
        Australia[3].count,
        Germany[3].count,
        United_States[3].count,
        India[3].count,
        France[3].count,
        United_kingdom[3].count,
        Canada[3].count,
        Pakistan[3].count
    ],
    textfont:{
        size:13,
        color:'white'
    },
    width: 0.18,
    marker:{
        color:'red'
    }
};  
// trace4.text = trace4.y;

let data = [
    trace1, 
    trace2, 
    trace3,
    trace4
];

let layout = {
    width: 1400,
    title: {
        text: 'Spotify 使用者訂閱類型比例（依國家）',
        font: {
            size: 20,
            color: '#333'
        },
        x: 0.5,
        xanchor: 'center'
    },
    barmode:'group'  ,
    bargap:0.25,       
    yaxis: {
      range: [18, 30],    
      title: '%'
    },
    xaxis: {
    tickangle: 0 ,
    automargin: true,    
     categoryorder: "array",
    categoryarray: [
      "Australia", "Germany", "United_States",
      "India", "France", "United_Kingdom",
      "Canada", "Pakistan"
    ],
    tickfont: {
      size: 14          
    }
  },

  yaxis: {
    range: [15, 30],
    title: '%'
  }
};



Plotly.newPlot('myGraph', data, layout);

function unpack(rows, key) {
    return rows.map(function (row) {
        return row[key];
    });
}
