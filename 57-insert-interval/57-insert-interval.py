class Solution:
	def insert(self, n: List[List[int]], n2: List[int]) -> List[List[int]]:
		n.append(n2)
		# print(n)
		a=len(n)
		if a<=1:
			return n
		i=0
		n.sort()
		ans=[]
		while i<a-1:
			if n[i][1]>=n[i+1][0]:
				n[i+1][0]=n[i][0]
				if n[i][1]>=n[i+1][1]:
					n[i+1][1]=n[i][1]
				i+=1
			else:
				ans.append(n[i])
				i+=1
			if i==a-1:
				ans.append(n[i])
		return ans