class ArrayWrapper {
    private nums: number[];
    private sum: number = 0;
    constructor(nums: number[]) {
        this.nums = nums;
        this.sum = nums.reduce((acc, curr) => acc + curr, 0);
    }
    
    valueOf(): number {
        return this.sum;
    }
    
    toString(): string {
        return `[${this.nums.join(',')}]`;
    }
};

/**
 * const obj1 = new ArrayWrapper([1,2]);
 * const obj2 = new ArrayWrapper([3,4]);
 * obj1 + obj2; // 10
 * String(obj1); // "[1,2]"
 * String(obj2); // "[3,4]"
 */