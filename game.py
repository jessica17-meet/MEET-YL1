from meet import *
import random
cells=[]
colors=['pink','yellow','blue','red']
cells_num=0
for i in range (30):
    ball1={'radius':random.randint(10,50), 'x':random.randint(5,200), 'y':random.randint(10,200), 'dy':random.uniform(-2,4), 'dx':random.uniform(2,-4), 'color': random.choice (colors) , 'shape' : 'circle'}
    circle1 = create_cell(ball1)
    cells.append(circle1)
    cells_num= cells_num+1

user_cell={'radius':random.randint(5,50), 'x':random.randint(5,200), 'y' :random.randint(10,200),'dy' :random.uniform(1,3),'dx' :random.uniform (1,4) ,'color' : 'black'}
t=create_cell(user_cell)
cells.append(t)

def limits(cells):
    for cell in cells:
        width=get_screen_width()
        height=get_screen_height()
        x=cell.xcor
        y=cell.ycor()

        if (cell.xcor() > width):
            cell.set_dx(-cell.get_dx())
        if (cell.ycor() > height):
            cell.set_dy(-cell.get_dy())   
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               
        if (cell.xcor() < -width):
            cell.set_dx(-cell.get_dx())
        if (cell.ycor() < -height):
            cell.set_dy(-cell.get_dy())


while (True):					
	move_cells(cells)
	limits(cells)
	dx,dy =  get_user_direction(t)
	t.set_dx(dx)
	t.set_dy(dy)
	#for circle in t: 
	#for other in t :
		#distance = ((cell.xcor()-other.xcor())**2+(cell.ycor()-other.ycor()**2)**0.5
		#if distance < cell.get_radius():
		#if cell.get_radius() > other.get_radius():
		#if other== z:
			#write('game over!) , al 
	for circle1 in cells:	
		if (circle1 != t):
			a=t.xcor()
			b=t.ycor()
			r=t.xcor()
			c=circle1.xcor()
			d=circle1.ycor
			r2=circle1.get_radius()
			if((a-c)**2+(b-d)**2)**0.5<=(r+r2):
				if (r>r2):
					circle1.goto(get_random_x(),get_random_y())

					t.set_raduis(r+0.5*r2)
meet.mainloop()
