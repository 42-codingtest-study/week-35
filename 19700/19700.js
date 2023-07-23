//문제: 19700
const fs = require("fs");
const filePath = process.platform === "linux" ? "/dev/stdin" : "./input.txt";
let input = fs.readFileSync(filePath).toString().trim().split("\n");

solution(input);
function solution(input) {
  let n = +input.shift();
  const arr = input
    .map((e) => e.split(" ").map(Number))
    .sort((a, b) => b[0] - a[0]);
  //   console.log(arr);
  const answer_list = [[arr[0][0]]];
  const check_list = (k, list) => {
    list.sort((a, b) => a.length - b.length);
    if (list[0].length ?? 0 < k) return 0;
    else return 1;
  };

  arr.forEach((e) => {
    let k = check_list(e[1], answer_list);
    console.log(k);
    if (!k) {
      answer_list.push([e[0]]);
    } else {
      answer_list[0].push(e[0]);
    }
    console.log(answer_list);
  });
}
