class StudentInfo{
	public String name1 = "Zack Dewan";
	public String name2 = "Daniel Olukiyesi";

	public int studentNumber1 = "8710898";

	public int studentNumber2 = "8696093";

	public String courseCode1 = "ITI1121 B";
	public String courseCode2 = "ITI1121 A00";

	int assignment = 1;

	public static void main(String[] args){
		display()

	}


	public static void display(){
		System.out.println("Author : "+name1 + " and "+ name2);
		System.out.println(" Student number : "+studentNumber1+ " and "+studentNumber2);
		System.out.println("Course: "+ courseCode1+ " and "+ courseCode2);
		System.out.println("Assignment :" + assignment);


	}

	
}