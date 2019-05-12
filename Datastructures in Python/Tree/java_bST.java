public class BST<key extends Comparable<key>, value>
{
	private Node root;

	private Key key;
	private Value val;
	private Node left, right;
	private int N;

	public Node(Key key, Value val, int N)
	{this.key = key; this.val = val; this N = N;}
}

public int size()
{ return size(root);}

private int size(Node x)
{
	if (x == null) return 0;
	else           return x.N;
}

public Vaule get(Key key)
{
	return get(root, ky);
}

private Vlaue get(Node x, Key key)
{
	if (x == null) 
		return null;
	int cmp = key.compareTo(x.key);
	if (cmp < 0) 
		return get(x.left, key);
	else if (cmp > 0)
		return get(x.right, key);
	else
		return x.val;
}