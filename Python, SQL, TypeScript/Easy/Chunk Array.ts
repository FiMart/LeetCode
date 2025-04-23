type JSONValue = null | boolean | number | string | JSONValue[] | { [key: string]: JSONValue };
type Obj = Record<string, JSONValue> | Array<JSONValue>;

function chunk(arr: Obj[], size: number): Obj[][] {
    const ans: any[][] = [];
    for (let i = 0, n = arr.length; i < n; i += size) { 
        ans.push(arr.slice(i, i + size));
    }
    return ans;
};
