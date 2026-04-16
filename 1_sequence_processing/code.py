from typing import List, Union
import numpy.typing as npt
import numpy as np

def base_count(fastafile: str) -> List[int]:
    # 課題 1-1

    counts = {'A':0, 'T':0, 'G':0, 'C':0}
    with open(fastafile, 'r') as f:
        for line in f:
            if line.startswith('>'):
                continue
            line = line.strip().upper()

            for base in line:
                if base in counts:
                    counts[base] +=1
    return [counts['A'], counts['C'], counts['G'], counts['T']] # A, T, G, C

def gen_rev_comp_seq(fastafile: str) -> str:
    # 課題 1-2
    comp = {'A':'T','T':'A','G':'C','C':'G'}
    seq = ""

    with open(fastafile, 'r') as f:
        for line in f:
            if line.startswith('>'):
                continue
            seq += line.strip().upper()

    reverse = ""
    for base in reversed(seq):
        if base in comp:
            reverse += comp[base]
        else:
            reverse += base
    return reverse

def calc_gc_content(fastafile: str, window: int=1000, step: int=300) -> Union[npt.NDArray[np.float_], List[float]]:
    # 課題 1-3
    # 値を出力するところまで。matplotlibを使う部分は別途実装してください。
    seq = ""
    with open(fastafile, 'r') as f:
        for line in f:
            if line.startswith('>'):
                continue
            seq += line.strip().upper()
    
    results = []
    for i in range(0, len(seq) - window + 1, step):
        sub_seq = seq[i, i+window]
        counts = sub_seq.count('G') + sub_seq.count('C')
        results.append((counts/window)*100)
    return results

def search_motif(fastafile: str, motif: str) -> List[str]:
    # 課題 1-4
    seq = ""

    with open(fastafile, 'r') as f:
        for line in f:
            if line.startswith('>'):
                continue
            seq += line.strip().upper()

    results: List[str] = [] 
    for i in range(0, len(seq)-len(motif) + 1):
        if seq[i:i+len(motif)-1] == motif:
            results.append(('F', i))

    revseq = gen_rev_comp_seq(fastafile)
    for i in range(0, len(revseq)-len(motif) + 1):
        if revseq[i:i+len(motif)-1] == motif:
            results.append(('R', len(revseq)-i+1))
    return results

def translate(fastafile: str) -> List[str]:
    # 課題 1-5
    
    return []

if __name__ == "__main__":
    filepath = "data/NT_113952.1.fasta"
    # 課題 1-1
    print(base_count(filepath))
    # 課題 1-2
    print(gen_rev_comp_seq(filepath))
    # 課題 1-3
    print(calc_gc_content(filepath))
    # 課題 1-4
    print(search_motif(filepath, "ATG"))
    # 課題 1-5
    print(translate(filepath))
