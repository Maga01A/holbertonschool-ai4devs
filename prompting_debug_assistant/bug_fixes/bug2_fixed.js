function calculateAverage(numbers) {
    let sum = 0;

    for (let i = 0; i < numbers.length; i++) {
        sum += numbers[i];
    }

    return sum / numbers.length;
}

const nums = [10, 20, 30, 40];
console.log(calculateAverage(nums)); // 25